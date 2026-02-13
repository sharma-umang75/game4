import streamlit as st
from datetime import datetime
from database import (
    create_game, get_game_by_id, update_game_status, get_available_games, 
    get_all_games, delete_game, update_game_partner, get_all_questions, get_user_guesses
)
from utils import format_time_ago, get_username_by_id, BATCH_SIZE
from questions import show_answering_phase, show_guessing_phase, show_results_phase

def show_game_lobby():
    """Display the game lobby"""
    st.header("🎮 Game Lobby")
    
    # Manual refresh button at the top
    col_refresh, col_info = st.columns([1, 5])
    with col_refresh:
        if st.button("🔄 Refresh Lobby"):
            st.session_state.last_refresh = datetime.now()
            st.rerun()
    with col_info:
        st.write("Auto-refreshes every 10 seconds")
    
    # Add auto-refresh mechanism
    if 'last_refresh' not in st.session_state or st.session_state.last_refresh is None:
        st.session_state.last_refresh = datetime.now()
    
    # Auto-refresh every 10 seconds
    if (datetime.now() - st.session_state.last_refresh).seconds > 10:
        st.session_state.last_refresh = datetime.now()
        st.rerun()
    
    # Get all available games (waiting and answering)
    all_available_games = get_available_games()
    
    # Get all games created by current user (regardless of status)
    all_my_games = get_all_games()
    my_games = []
    for game in all_my_games:
        game_id, user1_id, user2_id, status, batch_index, created_at = game
        if user1_id == st.session_state.current_user[0]:
            my_games.append(game)
    
    # Debug info
    with st.expander("Debug Info"):
        st.write(f"Current User ID: {st.session_state.current_user[0]}")
        st.write(f"Total available games: {len(all_available_games)}")
        st.write(f"My total games: {len(my_games)}")
        st.write("=== All Available Games ===")
        for game in all_available_games:
            game_id, user1_id, user2_id, status, batch_index, created_at = game
            st.write(f"Game {game_id}: User1={user1_id}, User2={user2_id}, Status={status}, Batch={batch_index}")
            st.write(f"  - Is my game? {user1_id == st.session_state.current_user[0]}")
            st.write(f"  - Has partner? {user2_id is not None}")
        
        st.write("=== Filtering Logic ===")
        available_games = []
        for game in all_available_games:
            game_id, user1_id, user2_id, status, batch_index, created_at = game
            # Skip if this is the current user's game
            if user1_id == st.session_state.current_user[0]:
                st.write(f"Skipping game {game_id} - it's my game")
                continue
            # Skip if game already has two users
            if user2_id is not None:
                st.write(f"Skipping game {game_id} - already has partner")
                continue
            # Only show games that are waiting for a partner
            st.write(f"Adding game {game_id} to available games")
            available_games.append(game)
        
        st.write(f"Final available games count: {len(available_games)}")
    
    # Separate available games (excluding user's own games and games that are full)
    available_games = []
    for game in all_available_games:
        game_id, user1_id, user2_id, status, batch_index, created_at = game
        # Skip if this is the current user's game
        if user1_id == st.session_state.current_user[0]:
            continue
        # Skip if game already has two users
        if user2_id is not None:
            continue
        # Only show games that are waiting for a partner
        available_games.append(game)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🆕 Create New Game")
        st.write("Start a new game and wait for a friend to join!")
        
        # Batch selection
        st.write("**Select Batch to Play:**")
        total_questions = len(get_all_questions())
        st.write(f"DEBUG: Total questions in DB: {total_questions}")
        num_batches = (total_questions + BATCH_SIZE - 1) // BATCH_SIZE
        st.write(f"DEBUG: Number of batches: {num_batches}")
        batch_options = {}
        for i in range(num_batches):
            start_q = i * BATCH_SIZE + 1
            end_q = min((i + 1) * BATCH_SIZE, total_questions)
            batch_options[i] = f"🎯 Batch {i+1} (Questions {start_q}-{end_q})"
        selected_batch = st.radio("Choose a batch:", list(batch_options.values()))
        batch_index = list(batch_options.keys())[list(batch_options.values()).index(selected_batch)]
        
        if st.button("Create Game", type="primary"):
            game_id = create_game(st.session_state.current_user[0], None, batch_index)
            st.session_state.current_game = game_id
            st.session_state.current_batch_index = batch_index
            st.session_state.user_answers = {}
            st.session_state.user_guesses = {}
            st.rerun()
    
    with col2:
        st.subheader("🎯 Join Existing Game")
        
        if available_games:
            st.write(f"**{len(available_games)} available games:**")
            
            for i, game in enumerate(available_games):
                game_id, user1_id, user2_id, status, batch_index, created_at = game
                
                creator_name = get_username_by_id(user1_id)
                
                if creator_name:
                    # Show different status based on game state
                    if status == "waiting":
                        status_text = "⏳ Waiting for players"
                    elif status == "answering":
                        status_text = "📝 In progress - answering"
                    else:
                        status_text = f"📊 {status}"
                    
                    with st.container():
                        col_a, col_b = st.columns([3, 1])
                        with col_a:
                            st.write(f"👤 **{creator_name}'s game**")
                            st.write(f"⏰ {format_time_ago(created_at)}")
                            st.write(status_text)
                        with col_b:
                            if st.button("Join", key=f"join_{game_id}"):
                                # Update game with second user
                                update_game_partner(game_id, st.session_state.current_user[0])
                                
                                st.session_state.current_game = game_id
                                st.session_state.last_known_status = "answering"
                                st.session_state.current_batch_index = batch_index
                                st.rerun()
                    
                    st.divider()
        else:
            st.info("🔍 No available games. Create a new one!")
    
    # Show user's own games
    if my_games:
        st.markdown("---")
        st.subheader("🎮 My Games")
        
        for game in my_games:
            game_id, user1_id, user2_id, status, batch_index, created_at = game
            
            with st.container():
                col_a, col_b, col_c = st.columns([2, 1, 1])
                with col_a:
                    st.write(f"👤 **Your game**")
                    
                    st.write(f"⏰ {format_time_ago(created_at)}")
                    st.write(f"📊 Status: {status}")
                    if user2_id:
                        partner_name = get_username_by_id(user2_id)
                        if partner_name != 'Unknown':
                            st.write(f"👥 Partner: {partner_name}")
                            st.write("✅ Game is ready!")
                    else:
                        st.write("⏳ Waiting for someone to join...")
                with col_b:
                    if st.button("Continue", key=f"continue_{game_id}"):
                        st.session_state.current_game = game_id
                        st.session_state.current_batch_index = batch_index
                        st.rerun()
                with col_c:
                    # Allow deletion of any game created by the user
                    if st.button("🗑️ Delete", key=f"delete_{game_id}", type="secondary"):
                        # Add confirmation for games in progress
                        if status != "waiting":
                            st.warning("⚠️ This will delete the game permanently. Your partner will lose access!")
                        delete_game(game_id)
                        # If this was the current game, clear it
                        if st.session_state.current_game == game_id:
                            st.session_state.current_game = None
                            st.session_state.current_question_index = 0
                            st.session_state.user_answers = {}
                            st.session_state.user_guesses = {}
                        st.success("Game deleted successfully!")
                        st.rerun()
                
                st.divider()
    
    # Manual refresh button is now at the top

def show_game_page(game):
    """Display the main game page"""
    import streamlit as st
    from questions import show_answering_phase, show_guessing_phase, show_results_phase
    
    game_id, user1_id, user2_id, status, batch_index, created_at = game
    current_user_id = st.session_state.current_user[0]
    
    # Always get fresh game data to detect changes
    fresh_game = get_game_by_id(game_id)
    if fresh_game:
        game_id, user1_id, user2_id, status, batch_index, created_at = fresh_game
    
    # Auto-refresh mechanism for waiting phase
    if status == "waiting":
        if 'game_last_check' not in st.session_state or st.session_state.game_last_check is None:
            st.session_state.game_last_check = datetime.now()
        
        # Refresh every 3 seconds when waiting
        if (datetime.now() - st.session_state.game_last_check).seconds > 3:
            st.session_state.game_last_check = datetime.now()
            # Get fresh game data
            fresh_game = get_game_by_id(game_id)
            if fresh_game and fresh_game[3] != status:  # Status changed
                st.rerun()
    
    # Auto-refresh mechanism for answering phase
    if status == "answering":
        if 'answering_last_check' not in st.session_state or st.session_state.answering_last_check is None:
            st.session_state.answering_last_check = datetime.now()
        
        # Refresh every 3 seconds when answering
        if (datetime.now() - st.session_state.answering_last_check).seconds > 3:
            st.session_state.answering_last_check = datetime.now()
            # Get fresh game data
            fresh_game = get_game_by_id(game_id)
            if fresh_game and fresh_game[3] != status:  # Status changed
                st.rerun()
    
    # Determine which user we are
    is_user1 = current_user_id == user1_id
    partner_id = user2_id if is_user1 else user1_id
    
    # Check if game state has changed and refresh if needed
    if status == "answering" and st.session_state.get('last_known_status') != status:
        st.session_state.current_question_index = 0
        st.session_state.last_known_status = status
        st.rerun()
    
    if status == "guessing" and st.session_state.get('last_known_status') != status:
        st.session_state.current_question_index = 0
        st.session_state.last_known_status = status
        st.rerun()
    
    # Get partner info
    partner_name = get_username_by_id(partner_id) if partner_id else 'Waiting for player...'
    
    st.header(f"Game with {partner_name}")
    
    # Add exit game button and refresh
    col1, col2, col3 = st.columns([1, 1, 6])
    with col1:
        if st.button("🚪 Exit Game", key="exit_game"):
            st.session_state.current_game = None
            st.session_state.current_question_index = 0
            st.session_state.user_answers = {}
            st.session_state.user_guesses = {}
            st.rerun()
    with col2:
        if st.button("🔄 Refresh", key="refresh_game"):
            st.rerun()
    
    # Debug info (remove in production)
    with st.expander("Debug Info"):
        st.write(f"Game ID: {game_id}")
        st.write(f"User1 ID: {user1_id}")
        st.write(f"User2 ID: {user2_id}")
        st.write(f"Current User ID: {current_user_id}")
        st.write(f"Status: {status}")
        st.write(f"Is User1: {is_user1}")
        st.write(f"Partner ID: {partner_id}")
    
    if status == "waiting":
        # Check if both users are now present
        if user1_id and user2_id:
            st.info("✅ Both players are here! Game starting...")
            # Auto-transition to answering phase
            update_game_status(game_id, "answering")
            st.rerun()
        elif is_user1 and not user2_id:
            st.info("⏳ Waiting for another player to join...")
            st.write("Share this game with a friend so they can join!")
            st.write("💡 Tip: The page will auto-refresh every 3 seconds")
        elif not is_user1 and not user2_id:
            st.info("🎉 You've joined the game! Waiting for the game creator to start...")
            st.write("💡 Tip: The page will auto-refresh every 3 seconds")
        
        if st.button("Cancel and return to lobby"):
            st.session_state.current_game = None
            st.rerun()
    
    elif status == "answering":
        show_answering_phase(game_id, current_user_id)
    
    elif status == "guessing":
        show_guessing_phase(game_id, current_user_id, partner_id)
    
    elif status == "completed":
        show_results_phase(game_id, current_user_id, partner_id, user1_id, user2_id)

import streamlit as st
from database import init_db, cleanup_database, get_database_stats, get_game_by_id
from auth import (
    show_login_page, show_register_page, show_user_sidebar, 
    restore_user_from_url, init_session_state, is_authenticated
)
from questions import initialize_questions_if_empty
from lobby import show_game_lobby, show_game_page

def main():
    st.set_page_config(page_title="Question Answering Game", page_icon="🎮", layout="wide")
    
    # Initialize database
    init_db()
    
    # Load sample questions if database is empty
    initialize_questions_if_empty()
    
    # Initialize session state
    init_session_state()
    
    # Try to restore user from browser storage
    restore_user_from_url()
    
    st.title("🎮 Question Answering Game")
    st.write("Connect with a friend and see how well you know each other!")
    
    # Sidebar for user info and admin tools
    show_user_sidebar()
    show_admin_sidebar()
    
    # Main content routing
    if not is_authenticated():
        if st.session_state.show_register:
            show_register_page()
        else:
            show_login_page()
    elif not st.session_state.current_game:
        show_game_lobby()
    else:
        game = get_game_by_id(st.session_state.current_game)
        if game:
            show_game_page(game)
        else:
            st.session_state.current_game = None
            st.rerun()

def show_admin_sidebar():
    """Display admin tools in sidebar"""
    with st.sidebar:
        st.markdown("---")
        st.header("🔧 Admin Tools")
        
        # Database cleanup section
        with st.expander("Database Management"):
            st.warning("⚠️ This will delete all data!")
            if st.button("🗑️ Clean Up Database", type="secondary"):
                cleanup_database()
                # Clear session state after cleanup
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
            
            # Show database stats
            stats = get_database_stats()
            st.write(f"👥 Users: {stats['users']}")
            st.write(f"🎮 Games: {stats['games']}")
            st.write(f"❓ Questions: {stats['questions']}")

if __name__ == "__main__":
    main()

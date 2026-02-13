import streamlit as st
from database import create_user, get_user_by_username, authenticate_user

def show_login_page():
    """Display the login page"""
    st.header("🔐 Login")
    
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        if st.form_submit_button("Login", type="primary"):
            if username and password:
                user = authenticate_user(username, password)
                if user:
                    st.session_state.current_user = user
                    st.success(f"Welcome back, {username}!")
                    
                    # Set URL parameters for persistence
                    st.query_params['user_id'] = user[0]
                    st.query_params['username'] = user[1]
                    
                    st.rerun()
                else:
                    st.error("Invalid username or password")
            else:
                st.error("Please enter both username and password")
    
    st.markdown("---")
    st.write("Don't have an account?")
    if st.button("Register", type="secondary"):
        st.session_state.show_register = True
        st.rerun()

def show_register_page():
    """Display the registration page"""
    st.header("📝 Register")
    
    with st.form("register_form"):
        username = st.text_input("Choose Username", key="register_username")
        email = st.text_input("Email", key="register_email")
        password = st.text_input("Password", type="password", key="register_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        
        if st.form_submit_button("Register", type="primary"):
            if username and email and password:
                if password != confirm_password:
                    st.error("Passwords do not match!")
                else:
                    # Check if user already exists
                    existing_user = get_user_by_username(username)
                    
                    if existing_user:
                        st.error("Username already exists! Please choose another.")
                    else:
                        # Create new user with password
                        user_id = create_user(username, email, password)
                        if user_id:
                            # Get the full user data from database to ensure correct format
                            user = get_user_by_username(username)
                            st.session_state.current_user = user
                            st.success(f"Welcome, {username}! Registration successful.")
                            
                            # Set URL parameters for persistence
                            st.query_params['user_id'] = user_id
                            st.query_params['username'] = username
                            
                            st.rerun()
                        else:
                            st.error("Email already exists! Please use another email.")
            else:
                st.error("Please fill in all fields!")
    
    st.markdown("---")
    st.write("Already have an account?")
    if st.button("Login", type="secondary"):
        st.session_state.show_register = False
        st.rerun()

def show_user_sidebar():
    """Display user information in sidebar"""
    with st.sidebar:
        st.header("User Info")
        
        if st.session_state.current_user:
            st.success(f"Logged in as: {st.session_state.current_user[1]}")
            if st.button("Logout"):
                # Clear URL parameters
                st.query_params.clear()
                
                # Clear all session state
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
        else:
            st.info("Not logged in")

def restore_user_from_url():
    """Try to restore user from browser URL parameters"""
    if not st.session_state.current_user:
        # Check URL parameters for user restoration
        query_params = st.query_params
        if 'user_id' in query_params and 'username' in query_params:
            try:
                from database import get_user_by_id
                user_id = query_params['user_id']
                username = query_params['username']
                # Verify user exists in database
                user = get_user_by_id(user_id)
                
                if user and user[1] == username:
                    st.session_state.current_user = user
                    st.rerun()
            except:
                pass

def init_session_state():
    """Initialize session state variables"""
    session_vars = {
        'current_user': None,
        'current_game': None,
        'current_question_index': 0,
        'current_batch_index': 0,  # Track which batch (0, 1, 2 for 30 questions)
        'user_answers': {},
        'user_guesses': {},
        'show_register': False,
        'last_refresh': None,
        'game_last_check': None,
        'last_known_status': None
    }
    
    for key, default_value in session_vars.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

def is_authenticated():
    """Check if user is authenticated"""
    return st.session_state.current_user is not None

def get_current_user():
    """Get current user data"""
    return st.session_state.current_user

def get_current_user_id():
    """Get current user ID"""
    if st.session_state.current_user:
        return st.session_state.current_user[0]
    return None

def get_current_username():
    """Get current username"""
    if st.session_state.current_user:
        return st.session_state.current_user[1]
    return None

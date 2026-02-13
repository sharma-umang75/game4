import sqlite3
import uuid
import hashlib
import os

def init_db():
    """Initialize the database with all required tables"""
    conn = sqlite3.connect('qa_game.db')
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Add password_hash column if it doesn't exist (for existing databases)
    try:
        cursor.execute('ALTER TABLE users ADD COLUMN password_hash TEXT')
        # Update existing users with default password
        cursor.execute('UPDATE users SET password_hash = ? WHERE password_hash IS NULL', 
                      (hashlib.sha256("default123".encode()).hexdigest(),))
    except sqlite3.OperationalError:
        # Column already exists
        pass
    
    # Create questions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id TEXT PRIMARY KEY,
            question_text TEXT NOT NULL,
            options TEXT NOT NULL, -- JSON array of 4 options
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create games table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id TEXT PRIMARY KEY,
            user1_id TEXT NOT NULL,
            user2_id TEXT,
            status TEXT DEFAULT 'waiting', -- waiting, answering, guessing, completed
            batch_index INTEGER DEFAULT 0, -- Which batch this game is using
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user1_id) REFERENCES users (id),
            FOREIGN KEY (user2_id) REFERENCES users (id)
        )
    ''')
    
    # Add batch_index column if it doesn't exist (for existing databases)
    try:
        cursor.execute('ALTER TABLE games ADD COLUMN batch_index INTEGER DEFAULT 0')
    except sqlite3.OperationalError:
        # Column already exists
        pass
    
    # Create answers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS answers (
            id TEXT PRIMARY KEY,
            game_id TEXT NOT NULL,
            user_id TEXT NOT NULL,
            question_id TEXT NOT NULL,
            selected_option INTEGER NOT NULL,
            FOREIGN KEY (game_id) REFERENCES games (id),
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (question_id) REFERENCES questions (id)
        )
    ''')
    
    # Create guesses table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guesses (
            id TEXT PRIMARY KEY,
            game_id TEXT NOT NULL,
            user_id TEXT NOT NULL,
            question_id TEXT NOT NULL,
            guessed_option INTEGER NOT NULL,
            FOREIGN KEY (game_id) REFERENCES games (id),
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (question_id) REFERENCES questions (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_db_connection():
    """Get a database connection"""
    return sqlite3.connect('qa_game.db')

def cleanup_database():
    """Clean up and reset the entire database"""
    db_file = 'qa_game.db'
    
    if os.path.exists(db_file):
        os.remove(db_file)
    
    # Reinitialize database
    init_db()
    return True

def get_database_stats():
    """Get database statistics"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM games')
    game_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM questions')
    question_count = cursor.fetchone()[0]
    
    conn.close()
    
    return {
        'users': user_count,
        'games': game_count,
        'questions': question_count
    }

# User management functions
def create_user(username, email, password=None):
    """Create a new user"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Hash the password if provided
        if password:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
        else:
            password_hash = hashlib.sha256("default123".encode()).hexdigest()  # Default password
        
        user_id = str(uuid.uuid4())
        cursor.execute('INSERT INTO users (id, username, email, password_hash) VALUES (?, ?, ?, ?)', 
                      (user_id, username, email, password_hash))
        conn.commit()
        conn.close()
        return user_id
    except sqlite3.IntegrityError as e:
        conn.close()
        if "email" in str(e):
            return None  # Email already exists
        elif "username" in str(e):
            return None  # Username already exists
        else:
            raise e

def get_user_by_username(username):
    """Get user by username"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    """Get user by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def authenticate_user(username, password):
    """Authenticate user with username and password"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()
    
    if user and len(user) >= 4 and check_password_hash(user[3], password):
        return user
    return None

def check_password_hash(stored_hash, password):
    """Check if password matches stored hash"""
    hash_object = hashlib.sha256(password.encode())
    return hash_object.hexdigest() == stored_hash

# Game management functions
def create_game(user1_id, user2_id=None, batch_index=0):
    """Create a new game"""
    conn = get_db_connection()
    cursor = conn.cursor()
    game_id = str(uuid.uuid4())
    cursor.execute('INSERT INTO games (id, user1_id, user2_id, batch_index) VALUES (?, ?, ?, ?)', 
                  (game_id, user1_id, user2_id, batch_index))
    conn.commit()
    conn.close()
    return game_id

def get_game_by_id(game_id):
    """Get game by ID"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, user1_id, user2_id, status, batch_index, created_at FROM games WHERE id = ?', (game_id,))
    game = cursor.fetchone()
    conn.close()
    return game

def update_game_status(game_id, status):
    """Update game status"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE games SET status = ? WHERE id = ?', (status, game_id))
    conn.commit()
    conn.close()

def get_available_games():
    """Get games that are waiting for players OR in answering phase"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, user1_id, user2_id, status, batch_index, created_at FROM games WHERE status IN ("waiting", "answering") ORDER BY created_at DESC')
    games = cursor.fetchall()
    conn.close()
    return games

def get_all_waiting_games():
    """Get all games that are waiting for players"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, user1_id, user2_id, status, batch_index, created_at FROM games WHERE status = "waiting" ORDER BY created_at DESC')
    games = cursor.fetchall()
    conn.close()
    return games

def get_all_games():
    """Get all games"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, user1_id, user2_id, status, batch_index, created_at FROM games ORDER BY created_at DESC')
    games = cursor.fetchall()
    conn.close()
    return games

def delete_game(game_id):
    """Delete a game and all related records"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Delete related records first (answers and guesses)
    cursor.execute('DELETE FROM answers WHERE game_id = ?', (game_id,))
    cursor.execute('DELETE FROM guesses WHERE game_id = ?', (game_id,))
    
    # Delete the game
    cursor.execute('DELETE FROM games WHERE id = ?', (game_id,))
    
    conn.commit()
    conn.close()

def update_game_partner(game_id, user2_id):
    """Update game with second player and change status to answering"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE games SET user2_id = ?, status = "answering" WHERE id = ?', 
                  (user2_id, game_id))
    conn.commit()
    conn.close()

# Answer and guess management functions
def save_answer(game_id, user_id, question_id, selected_option):
    """Save user's answer to a question"""
    conn = get_db_connection()
    cursor = conn.cursor()
    answer_id = str(uuid.uuid4())
    cursor.execute('INSERT INTO answers (id, game_id, user_id, question_id, selected_option) VALUES (?, ?, ?, ?, ?)', 
                  (answer_id, game_id, user_id, question_id, selected_option))
    conn.commit()
    conn.close()

def save_guess(game_id, user_id, question_id, guessed_option):
    """Save user's guess about partner's answer"""
    conn = get_db_connection()
    cursor = conn.cursor()
    guess_id = str(uuid.uuid4())
    cursor.execute('INSERT INTO guesses (id, game_id, user_id, question_id, guessed_option) VALUES (?, ?, ?, ?, ?)', 
                  (guess_id, game_id, user_id, question_id, guessed_option))
    conn.commit()
    conn.close()

def get_user_answers(game_id, user_id):
    """Get all answers for a user in a game"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT question_id, selected_option FROM answers WHERE game_id = ? AND user_id = ?', 
                  (game_id, user_id))
    answers = cursor.fetchall()
    conn.close()
    return answers

def get_user_guesses(game_id, user_id):
    """Get all guesses for a user in a game"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT question_id, guessed_option FROM guesses WHERE game_id = ? AND user_id = ?', 
                  (game_id, user_id))
    guesses = cursor.fetchall()
    conn.close()
    return guesses

def get_answered_users_count(game_id):
    """Get count of distinct users who have answered in a game"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(DISTINCT user_id) FROM answers WHERE game_id = ?', (game_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_guessed_users_count(game_id):
    """Get count of distinct users who have guessed in a game"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(DISTINCT user_id) FROM guesses WHERE game_id = ?', (game_id,))
    count = cursor.fetchone()[0]
    conn.close()
    return count

def get_all_questions():
    """Get all questions from the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions')
    questions = cursor.fetchall()
    conn.close()
    return questions

def get_game_questions(game_id):
    """Get questions for a specific game based on its batch selection"""
    BATCH_SIZE = 10  # Define batch size directly
    
    # Get the game to find its batch index
    game = get_game_by_id(game_id)
    if not game:
        return []
    
    _, _, _, _, batch_index, _ = game  # Extract batch_index from game tuple
    
    # Convert batch_index to integer in case it's stored as string
    batch_index = int(batch_index)
    
    # Get all questions and filter to the selected batch
    all_questions = get_all_questions()
    start_index = batch_index * BATCH_SIZE
    end_index = start_index + BATCH_SIZE
    
    return all_questions[start_index:end_index]

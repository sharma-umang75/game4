from datetime import datetime

BATCH_SIZE = 10

def format_time_ago(created_at):
    """Format a timestamp as 'X minutes/hours ago'"""
    try:
        created_dt = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        time_diff = datetime.now() - created_dt
        minutes_ago = int(time_diff.total_seconds() / 60)
        if minutes_ago < 1:
            return "Just now"
        elif minutes_ago == 1:
            return "1 minute ago"
        elif minutes_ago < 60:
            return f"{minutes_ago} minutes ago"
        else:
            hours_ago = minutes_ago // 60
            if hours_ago == 1:
                return "1 hour ago"
            else:
                return f"{hours_ago} hours ago"
    except:
        return "Unknown time"

def get_username_by_id(user_id):
    """Get username by user ID"""
    from database import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT username FROM users WHERE id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 'Unknown'

def get_batch_questions(all_questions, batch_index):
    """Get questions for a specific batch"""
    start_index = batch_index * BATCH_SIZE
    end_index = start_index + BATCH_SIZE
    return all_questions[start_index:end_index]

def get_batch_info(batch_index, total_questions):
    """Get batch information for display"""
    total_batches = (total_questions + BATCH_SIZE - 1) // BATCH_SIZE
    start_question = batch_index * BATCH_SIZE + 1
    end_question = min((batch_index + 1) * BATCH_SIZE, total_questions)
    
    return {
        'batch_number': batch_index + 1,
        'total_batches': total_batches,
        'start_question': start_question,
        'end_question': end_question,
        'total_questions': total_questions
    }

def is_batch_complete(batch_questions, user_data):
    """Check if all questions in batch are completed"""
    return all(q_id in user_data for q_id, _, _, _ in batch_questions)

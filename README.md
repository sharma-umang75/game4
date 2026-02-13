# Question Answering Game

A web-based multiplayer question answering game built with Streamlit that allows two users to connect, answer questions, and guess each other's responses.

## Features

- **User Registration/Login**: Simple username and email authentication
- **Game Lobby**: Create new games or join existing ones
- **Question Phase**: Answer multiple-choice questions
- **Guessing Phase**: Try to guess what your partner answered
- **Results Display**: Compare answers and see how well you know each other
- **Real-time Updates**: Automatic progression through game phases

## Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **Database**: SQLite
- **Deployment**: Vercel (ready)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

## How to Play

1. **Login/Register**: Enter your username and email
2. **Create or Join Game**: Either create a new game and wait for a partner, or join an existing game
3. **Answer Questions**: Go through 5 multiple-choice questions
4. **Guess Partner's Answers**: Try to guess what your partner selected for each question
5. **View Results**: See how well you know each other!

## Database Schema

The application uses SQLite with the following tables:
- `users`: User information (id, username, email)
- `questions`: Question data (id, question_text, options)
- `games`: Game sessions (id, user1_id, user2_id, status)
- `answers`: User answers (game_id, user_id, question_id, selected_option)
- `guesses`: User guesses (game_id, user_id, question_id, guessed_option)

## Game States

1. **waiting**: Game created, waiting for second player
2. **answering**: Both players answering questions
3. **guessing**: Both players guessing partner's answers
4. **completed**: Game finished, showing results

## Deployment

The application is configured for Vercel deployment. Simply connect your repository to Vercel and it will automatically deploy the Streamlit app.

## Sample Questions

The app includes 5 sample questions about preferences:
- Favorite color
- Ideal vacation destination
- Favorite season
- Preferred way to relax
- Favorite type of food

You can easily add more questions by modifying the `load_sample_questions()` function or by adding questions directly to the database.

import json
import uuid
from database import get_db_connection, get_all_questions, save_answer, save_guess, get_user_answers, get_user_guesses, get_answered_users_count, get_guessed_users_count, update_game_status, get_user_by_id, get_game_by_id, get_game_questions

def load_sample_questions():
    """Load sample questions into the database"""
    sample_questions = [

{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow oral attention around your backside during foreplay?", "options": json.dumps(["Extremely arousing", "Very curious", "Only lightly", "Not comfortable"])},

{"id": str(uuid.uuid4()), "question_text": "Would you enjoy your partner using their tongue to tease your most sensitive back area?", "options": json.dumps(["Yes intensely", "Curious to try", "Only briefly", "Not interested"])},

{"id": str(uuid.uuid4()), "question_text": "How adventurous are you with oral exploration of your partner’s backside?", "options": json.dumps(["Very adventurous", "Moderately bold", "Only occasionally", "Prefer not"])},

{"id": str(uuid.uuid4()), "question_text": "How do you feel about combining oral pleasure with slow backdoor teasing?", "options": json.dumps(["Very intense", "Curious but cautious", "Only lightly", "Too much for me"])},

{"id": str(uuid.uuid4()), "question_text": "Would you explore deeper oral teasing of the backside with full trust?", "options": json.dumps(["Yes with trust", "Maybe once", "Only gently", "No"])},

{"id": str(uuid.uuid4()), "question_text": "How important is trust before exploring oral attention to your backside?", "options": json.dumps(["Completely essential", "Very important", "Somewhat important", "I would avoid it"])},

{"id": str(uuid.uuid4()), "question_text": "Do you find slow teasing around your back entrance highly erotic?", "options": json.dumps(["Yes very much", "Sometimes", "Only in certain moods", "Not really"])},

{"id": str(uuid.uuid4()), "question_text": "Would you enjoy switching between oral on your front and backside during intimacy?", "options": json.dumps(["Extremely exciting", "Very adventurous", "Only occasionally", "Prefer consistency"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow oral teasing?", "options": json.dumps(["Extremely arousing", "Very enjoyable", "Depends on mood", "Prefer direct intensity"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy giving oral as much as receiving?", "options": json.dumps(["Love both equally", "Prefer giving", "Prefer receiving", "Depends on connection"])},
{"id": str(uuid.uuid4()), "question_text": "What style of oral excites you most?", "options": json.dumps(["Slow and teasing", "Deep and intense", "Dominant control", "Playful switching"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about eye contact during oral?", "options": json.dumps(["Very hot", "Sometimes", "Only briefly", "Prefer focus without eye contact"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being guided physically during oral?", "options": json.dumps(["Yes confidently", "Sometimes", "Only gently", "Prefer not"])},
{"id": str(uuid.uuid4()), "question_text": "How adventurous are you with oral exploration?", "options": json.dumps(["Very adventurous", "Moderately bold", "Curious but cautious", "Prefer traditional"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about mutual oral pleasure at the same time?", "options": json.dumps(["Extremely intimate", "Very exciting", "Only sometimes", "Not my preference"])},
{"id": str(uuid.uuid4()), "question_text": "What excites you more during oral?", "options": json.dumps(["Slow buildup", "Intense rhythm", "Dominant energy", "Being teased repeatedly"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being praised during oral?", "options": json.dumps(["Yes very much", "Sometimes", "Only subtly", "Not important"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about oral in the shower?", "options": json.dumps(["Very hot", "Exciting but tricky", "Only occasionally", "Prefer dry settings"])},

{"id": str(uuid.uuid4()), "question_text": "How do you feel about shower intimacy overall?", "options": json.dumps(["Steamy and intense", "Romantic and slow", "Playful and fun", "Not my favorite"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being pressed against the shower wall?", "options": json.dumps(["Very arousing", "Sometimes", "Only gently", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow exploration with fingers?", "options": json.dumps(["Very intimate", "Extremely exciting", "Only with buildup", "Prefer other stimulation"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy fingers teasing before penetration?", "options": json.dumps(["Yes intensely", "Sometimes", "Only briefly", "Prefer direct action"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about deep finger exploration?", "options": json.dumps(["Very arousing", "Curious", "Only gently", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy having your hips guided during fingering?", "options": json.dumps(["Yes very much", "Sometimes", "Only lightly", "Prefer control myself"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow circular teasing?", "options": json.dumps(["Drives me wild", "Very enjoyable", "Depends on mood", "Prefer firmer touch"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being teased near your most sensitive area without immediate penetration?", "options": json.dumps(["Yes intensely", "Sometimes", "Only briefly", "Prefer direct stimulation"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about dominant finger control?", "options": json.dumps(["Extremely arousing", "Curious to try", "Only lightly", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy slow buildup before full intimacy?", "options": json.dumps(["Yes absolutely", "Sometimes", "Depends on mood", "Prefer quick escalation"])},

{"id": str(uuid.uuid4()), "question_text": "How do you feel about anal curiosity?", "options": json.dumps(["Very curious", "Open with trust", "Maybe one day", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "Would you explore anal play slowly with preparation?", "options": json.dumps(["Yes with trust", "Curious but cautious", "Only very gently", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about light external anal teasing?", "options": json.dumps(["Very arousing", "Curious", "Only briefly", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy slow progression during anal exploration?", "options": json.dumps(["Yes absolutely", "Only with patience", "Maybe once", "Not my preference"])},
{"id": str(uuid.uuid4()), "question_text": "How important is trust for anal intimacy?", "options": json.dumps(["Completely essential", "Very important", "Somewhat important", "I avoid it"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy being guided through anal exploration?", "options": json.dumps(["Yes with confidence", "Only slowly", "Maybe once", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about combining oral and anal teasing?", "options": json.dumps(["Extremely intense", "Very exciting", "Only lightly", "Too much"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being verbally encouraged during anal play?", "options": json.dumps(["Yes very much", "Sometimes", "Only subtly", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about trying new boundaries in anal intimacy?", "options": json.dumps(["Very adventurous", "Curious", "Only cautiously", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy dominant control during anal exploration?", "options": json.dumps(["Yes with trust", "Sometimes", "Only gently", "No"])},

{"id": str(uuid.uuid4()), "question_text": "How do you feel about licking your partner's body slowly?", "options": json.dumps(["Very arousing", "Playful and fun", "Only in moments", "Not my style"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy your partner licking your lower body slowly?", "options": json.dumps(["Extremely intimate", "Very exciting", "Only sometimes", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow teasing around your hips and backside?", "options": json.dumps(["Drives me wild", "Very enjoyable", "Depends on mood", "Prefer direct touch"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy attention focused on your backside?", "options": json.dumps(["Yes very much", "Sometimes", "Only lightly", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow licking during foreplay?", "options": json.dumps(["Extremely arousing", "Very intimate", "Occasionally", "Not my preference"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy being kissed and licked from neck to lower body?", "options": json.dumps(["Yes intensely", "Very much", "Sometimes", "Too overwhelming"])},
{"id": str(uuid.uuid4()), "question_text": "How adventurous are you with full-body oral exploration?", "options": json.dumps(["Very adventurous", "Moderately bold", "Curious but cautious", "Prefer traditional"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy slow teasing around intimate curves?", "options": json.dumps(["Yes very much", "Sometimes", "Only briefly", "Prefer direct action"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about prolonged teasing before penetration?", "options": json.dumps(["Makes it explosive", "Very enjoyable", "Depends on mood", "Prefer faster escalation"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy being slowly explored with mouth and fingers together?", "options": json.dumps(["Extremely intense", "Very exciting", "Only sometimes", "Too much stimulation"])},

{"id": str(uuid.uuid4()), "question_text": "How do you feel about combining shower intimacy with oral teasing?", "options": json.dumps(["Very hot", "Exciting to try", "Only occasionally", "Prefer separate"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being bent slightly while teased from behind?", "options": json.dumps(["Very arousing", "Sometimes", "Only gently", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about slow backdoor teasing during foreplay?", "options": json.dumps(["Extremely intense", "Curious", "Only lightly", "No interest"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy oral attention focused solely on your most sensitive area?", "options": json.dumps(["Yes completely", "Very much", "Only briefly", "Prefer variety"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about intense stimulation right before climax?", "options": json.dumps(["Makes it explosive", "Very enjoyable", "Only sometimes", "Too overwhelming"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy switching between oral and penetration repeatedly?", "options": json.dumps(["Yes very much", "Sometimes", "Only occasionally", "Prefer consistency"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about deep surrender during oral?", "options": json.dumps(["Extremely arousing", "Only with trust", "Sometimes", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "Would you explore intense pleasure focused entirely on your lower body?", "options": json.dumps(["Absolutely", "With the right mood", "Maybe once", "Prefer balanced focus"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about pushing limits in oral or anal intimacy?", "options": json.dumps(["Very adventurous", "Curious", "Only cautiously", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "How far are you willing to explore new intimate boundaries?", "options": json.dumps(["Very far with trust", "Moderately bold", "Slightly curious", "Prefer staying safe"])},
{"id": str(uuid.uuid4()), "question_text": "Where do you love being kissed the most?", "options": json.dumps(["Neck", "Lips slowly", "Chest and torso", "Everywhere intensely"])},
{"id": str(uuid.uuid4()), "question_text": "How do you like intimacy to begin?", "options": json.dumps(["Slow teasing", "Deep eye contact", "Sudden pull closer", "Whispered desire"])},
{"id": str(uuid.uuid4()), "question_text": "What turns you on the fastest?", "options": json.dumps(["Confident touch", "Dominant tone", "Slow buildup", "Being watched"])},
{"id": str(uuid.uuid4()), "question_text": "How do you prefer being undressed?", "options": json.dumps(["Slowly teased", "Confidently stripped", "Playfully", "With intense eye contact"])},
{"id": str(uuid.uuid4()), "question_text": "What kind of foreplay excites you most?", "options": json.dumps(["Long and sensual", "Rough and urgent", "Playful teasing", "Power exchange"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being dominated?", "options": json.dumps(["Yes completely", "Sometimes", "I prefer dominating", "Equal control"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about light restraint?", "options": json.dumps(["Very exciting", "Curious", "Only lightly", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "What kind of pace drives you wild?", "options": json.dumps(["Slow and deep", "Fast and intense", "Unpredictable rhythm", "Build then explode"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy teasing before climax?", "options": json.dumps(["Yes, a lot", "Sometimes", "Rarely", "Prefer immediate intensity"])},
{"id": str(uuid.uuid4()), "question_text": "How important is dirty talk?", "options": json.dumps(["Essential", "Adds heat", "Occasionally", "Prefer silence"])},

{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being pinned gently?", "options": json.dumps(["Very arousing", "Sometimes", "Only lightly", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about spontaneous quick intimacy?", "options": json.dumps(["Very exciting", "Sometimes fun", "Prefer planned", "Not into quickies"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy intimacy in a car?", "options": json.dumps(["Very thrilling", "Once in a while", "Only discreetly", "Prefer indoors"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about shower intimacy?", "options": json.dumps(["Steamy and hot", "Romantic", "Playful", "Too slippery"])},
{"id": str(uuid.uuid4()), "question_text": "What role excites you most?", "options": json.dumps(["Dominant", "Submissive", "Switch", "Equal"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being watched while intimate?", "options": json.dumps(["Yes intensely", "Sometimes", "Only with trust", "Prefer privacy"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about intense eye contact?", "options": json.dumps(["Very hot", "Sometimes", "Only during climax", "Prefer eyes closed"])},
{"id": str(uuid.uuid4()), "question_text": "What makes a kiss escalate fast?", "options": json.dumps(["Firm grip", "Breathing heavy", "Whispered words", "Being pulled closer"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy slow grinding before penetration?", "options": json.dumps(["Very much", "Sometimes", "Depends on mood", "Prefer direct"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about messy passion?", "options": json.dumps(["Very hot", "Sometimes", "Only private", "Prefer controlled"])},

{"id": str(uuid.uuid4()), "question_text": "Would you enjoy being marked lightly?", "options": json.dumps(["Yes", "Subtly only", "Maybe once", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "How intense do you like climax?", "options": json.dumps(["Slow overwhelming", "Wild explosion", "Dominant energy", "Mutual surrender"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy multiple rounds?", "options": json.dumps(["Absolutely", "If chemistry strong", "Rarely", "One intense round"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about oral pleasure?", "options": json.dumps(["Love giving and receiving", "Prefer receiving", "Prefer giving", "Depends on mood"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about climax control?", "options": json.dumps(["Very arousing", "Curious", "Only lightly", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy power exchange scenarios?", "options": json.dumps(["Very exciting", "Curious", "Only mild", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "How rough do you like intimacy?", "options": json.dumps(["Firm but safe", "Dominant and wild", "Playful struggle", "Prefer gentle"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy hair pulling?", "options": json.dumps(["Yes", "Light only", "Curious", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about spanking?", "options": json.dumps(["Very arousing", "Light only", "Curious", "No"])},
{"id": str(uuid.uuid4()), "question_text": "What builds tension fastest?", "options": json.dumps(["Whispers", "Firm grip", "Eye contact", "Slow teasing"])},

{"id": str(uuid.uuid4()), "question_text": "Do you enjoy finishing together intentionally?", "options": json.dumps(["Very intimate", "Exciting challenge", "Sometimes", "Not important"])},
{"id": str(uuid.uuid4()), "question_text": "Would you try outdoor intimacy?", "options": json.dumps(["Under stars", "Beach at night", "Private balcony", "Too risky"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about surrendering control?", "options": json.dumps(["Extremely hot", "Only with trust", "Rarely", "Never"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy controlling your partner?", "options": json.dumps(["Yes fully", "Sometimes", "Curious", "Not interested"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about light choking with consent?", "options": json.dumps(["Very arousing", "Curious", "Only lightly", "Not comfortable"])},
{"id": str(uuid.uuid4()), "question_text": "Do you like slow buildup or instant intensity?", "options": json.dumps(["Slow buildup", "Instant intensity", "Mix of both", "Depends on mood"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about deep passionate kissing?", "options": json.dumps(["Love it", "Sometimes", "Short bursts", "Not too much"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy being guided physically?", "options": json.dumps(["Yes", "Sometimes", "I prefer guiding", "Not really"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about climaxing loudly?", "options": json.dumps(["Love expressing", "Depends on mood", "Stay controlled", "Prefer quiet"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy edging for long time?", "options": json.dumps(["Yes intensely", "Sometimes", "Short edging", "No"])},

{"id": str(uuid.uuid4()), "question_text": "How dark do you like intimacy?", "options": json.dumps(["Very intense", "Moderately bold", "Playful only", "Keep it light"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy being completely taken over?", "options": json.dumps(["Yes", "Only sometimes", "Rarely", "No"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy intense grip during climax?", "options": json.dumps(["Yes", "Sometimes", "Light only", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about late night raw passion?", "options": json.dumps(["Very hot", "Sometimes", "Depends mood", "Prefer calm"])},
{"id": str(uuid.uuid4()), "question_text": "Would you enjoy dominance in public whispers?", "options": json.dumps(["Very exciting", "Sometimes", "Only subtle", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about being told what to do in bed?", "options": json.dumps(["Very arousing", "Sometimes", "I prefer telling", "Not into it"])},
{"id": str(uuid.uuid4()), "question_text": "Do you enjoy high tension before release?", "options": json.dumps(["Yes", "Sometimes", "Short only", "No"])},
{"id": str(uuid.uuid4()), "question_text": "How do you feel about intense physical closeness?", "options": json.dumps(["Love it", "Sometimes", "Depends mood", "Prefer space"])},
{"id": str(uuid.uuid4()), "question_text": "Would you experiment with new positions?", "options": json.dumps(["Always", "Sometimes", "Rarely", "Prefer classic"])},
{"id": str(uuid.uuid4()), "question_text": "How adventurous are you sexually?", "options": json.dumps(["Very adventurous", "Moderately", "Slightly", "Not much"])},
{
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about being teased right before climax?",
            "options": json.dumps(["It makes it more explosive", "I enjoy controlled teasing", "Only sometimes", "Prefer not to delay"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Do you enjoy being verbally dominated during sex?",
            "options": json.dumps(["Yes, very much", "Only in certain moods", "I prefer dominating", "Not into it"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about mutual oral pleasure?",
            "options": json.dumps(["Extremely intimate", "Very enjoyable", "Depends on mood", "Prefer traditional roles"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "What excites you more during oral?",
            "options": json.dumps(["Slow teasing build", "Deep intense rhythm", "Dominant control", "Switching control"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you prefer to be positioned during intense moments?",
            "options": json.dumps(["Pinned and controlled", "On top and dominant", "Side by side close", "Constant switching"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about hair pulling during sex?",
            "options": json.dumps(["Very arousing", "Light and playful", "Only sometimes", "Not comfortable"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Do you enjoy being lightly spanked?",
            "options": json.dumps(["Yes, it excites me", "Only gently", "Curious but unsure", "Not interested"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about being held firmly against a wall?",
            "options": json.dumps(["Very turned on", "Sometimes", "Only in private settings", "Not comfortable"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "What type of pace excites you most?",
            "options": json.dumps(["Slow and deep", "Fast and intense", "Unpredictable rhythm", "Build then explode"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about spontaneous quick intimacy?",
            "options": json.dumps(["Very exciting", "Sometimes fun", "Prefer planned moments", "Not into quickies"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Would you enjoy intimacy in a car at night?",
            "options": json.dumps(["Yes, very thrilling", "Only if discreet", "Maybe once", "Prefer indoors"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about outdoor intimacy under the stars?",
            "options": json.dumps(["Extremely hot", "Romantic and sensual", "Risky but exciting", "Too risky"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Do you like being guided physically during sex?",
            "options": json.dumps(["Yes, very much", "Sometimes", "I prefer guiding", "Not really"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about finishing together intentionally?",
            "options": json.dumps(["Very intimate", "Exciting challenge", "Sometimes possible", "Not important"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "What level of eye contact do you prefer during climax?",
            "options": json.dumps(["Intense eye lock", "Occasional glances", "Eyes closed", "Depends on mood"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about dominant restraint with consent?",
            "options": json.dumps(["Very arousing", "Curious to try", "Only lightly", "Not comfortable"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Do you enjoy being told what to do during sex?",
            "options": json.dumps(["Yes, very much", "Sometimes", "I prefer telling", "Not into commands"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about power exchange scenarios?",
            "options": json.dumps(["Extremely exciting", "Curious", "Only mild", "Not interested"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Would you enjoy being slowly undressed while watched?",
            "options": json.dumps(["Very arousing", "Sometimes", "Only with trust", "Prefer privacy"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How intense do you like foreplay?",
            "options": json.dumps(["Long and consuming", "Moderate build", "Short and direct", "Minimal foreplay"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Do you enjoy being held down gently during climax?",
            "options": json.dumps(["Yes, very much", "Sometimes", "Only lightly", "Not comfortable"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about surrendering control completely?",
            "options": json.dumps(["Extremely arousing", "Only with trust", "Rarely", "Not interested"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Would you enjoy controlling your partner's climax?",
            "options": json.dumps(["Yes, very much", "Sometimes", "Curious to try", "Not interested"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about slow grinding before penetration?",
            "options": json.dumps(["Very arousing", "Enjoyable tease", "Depends on mood", "Prefer direct action"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about intense rough sessions?",
            "options": json.dumps(["Love it", "Sometimes", "Only controlled", "Not my style"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "What excites you more at climax?",
            "options": json.dumps(["Dominant energy", "Mutual surrender", "Wild intensity", "Slow deep release"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about messy passion?",
            "options": json.dumps(["Very hot", "Sometimes", "Only private", "Prefer clean control"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "Would you enjoy being marked lightly during intimacy?",
            "options": json.dumps(["Yes, very arousing", "Only subtly", "Maybe once", "Not comfortable"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How do you feel about multiple climaxes in one session?",
            "options": json.dumps(["Very exciting", "Sometimes", "Rarely", "Prefer one strong climax"])
        },
        {
            "id": str(uuid.uuid4()),
            "question_text": "How deeply do you like to connect during sex?",
            "options": json.dumps(["Emotionally and physically intense", "Mostly physical", "Balanced mix", "Keep it light"])
        }
    ]
          
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Delete existing questions to replace with new ones
    cursor.execute('DELETE FROM questions')
    
    for question in sample_questions:
        cursor.execute('INSERT OR IGNORE INTO questions (id, question_text, options) VALUES (?, ?, ?)', 
                      (question["id"], question["question_text"], question["options"]))
    
    conn.commit()
    conn.close()

def show_answering_phase(game_id, current_user_id):
    """Display the answering phase - one question at a time"""
    import streamlit as st
    from database import get_game_questions
    
    st.subheader("Answer the Questions")
    
    # Debug information
    with st.expander("Debug Info - Answering Phase"):
        st.write(f"Current User ID: {current_user_id}")
        st.write(f"Current Question Index: {st.session_state.current_question_index}")
        st.write(f"Current Batch Index: {st.session_state.current_batch_index}")
    
    # Get questions for this specific game (already filtered by batch)
    questions = get_game_questions(game_id)
    total_questions = len(questions)
    
    if total_questions == 0:
        st.error("No questions available for this batch!")
        return
    
    # Display batch information
    st.write(f"**Answering {total_questions} questions**")
    st.write(f"Question {st.session_state.current_question_index + 1} of {total_questions}")
    
    # Check if we've completed all questions
    if st.session_state.current_question_index >= total_questions:
        # All questions completed - check if both users are done
        user1_guesses = get_user_guesses(game_id, user1_id)
        user2_guesses = get_user_guesses(game_id, user2_id)
        
        if len(user1_guesses) == total_questions and len(user2_guesses) == total_questions:
            # Both users completed - move to results
            update_game_status(game_id, "completed")
            st.success("Both users completed all guesses! Moving to results phase.")
            st.rerun()
        else:
            st.success("✅ You completed all guesses! Waiting for your partner...")
            return
    
    # Get current question
    question = questions[st.session_state.current_question_index]
    question_id, question_text, options_json, created_at = question
    options = json.loads(options_json)
    
    st.write(f"**Question {st.session_state.current_question_index + 1}:** {question_text}")
    
    # Check if already answered
    existing_answer = st.session_state.user_answers.get(question_id)
    default_index = existing_answer if existing_answer is not None else 0
    
    selected_option = st.radio(
        "Choose your answer:", 
        options, 
        key=f"answer_{question_id}",
        index=default_index
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Previous Question", disabled=st.session_state.current_question_index == 0):
            st.session_state.current_question_index -= 1
            st.rerun()
    
    with col2:
        if st.button("Next Question"):
            # Save answer
            option_index = options.index(selected_option)
            save_answer(game_id, current_user_id, question_id, option_index)
            st.session_state.user_answers[question_id] = option_index
            
            # Move to next question
            if st.session_state.current_question_index < total_questions - 1:
                st.session_state.current_question_index += 1
                st.rerun()
            else:
                # All questions completed - check if both users are done
                from database import get_answered_users_count
                answered_users = get_answered_users_count(game_id)
                
                if answered_users == 2:
                    from database import update_game_status
                    update_game_status(game_id, "guessing")
                    st.session_state.current_question_index = 0  # Reset for guessing phase
                    st.success("Both users completed all answers! Moving to guessing phase.")
                    st.rerun()
                else:
                    st.success("All answers completed! Waiting for your partner...")
    
    # Progress bar
    progress = (st.session_state.current_question_index + 1) / total_questions
    st.progress(progress)
    st.write(f"Progress: {st.session_state.current_question_index + 1}/{total_questions} questions")

def show_guessing_phase(game_id, current_user_id, partner_id):
    """Display the guessing phase - one question at a time"""
    import streamlit as st
    from database import get_game_questions, get_user_guesses, get_game_by_id, update_game_status
    
    st.subheader("Guess Your Partner's Answers")
    
    # Get questions for this specific game (already filtered by batch)
    questions = get_game_questions(game_id)
    total_questions = len(questions)
    
    if total_questions == 0:
        st.error("No questions available for this batch!")
        return
    
    # Get user IDs from game
    game = get_game_by_id(game_id)
    if game:
        _, user1_id, user2_id, _, batch_index, _ = game
    else:
        st.error("Game not found!")
        return
    
    # Check if both users have completed guessing
    user1_guesses = get_user_guesses(game_id, user1_id)
    user2_guesses = get_user_guesses(game_id, user2_id)
    if len(user1_guesses) == total_questions and len(user2_guesses) == total_questions:
        # Both completed - move to results
        update_game_status(game_id, "completed")
        st.success("Both users completed all guesses! Moving to results phase.")
        st.rerun()
    
    # Debug information
    with st.expander("Debug Info - Guessing Phase"):
        st.write(f"Current User ID: {current_user_id}")
        st.write(f"Partner ID: {partner_id}")
        st.write(f"Current Question Index: {st.session_state.current_question_index}")
        st.write(f"Current Batch Index: {st.session_state.current_batch_index}")
    
    # Display batch information
    st.write(f"**Guessing {total_questions} answers**")
    st.write(f"Question {st.session_state.current_question_index + 1} of {total_questions}")
    
    existing_guesses = get_user_guesses(game_id, current_user_id)
    
    # Check if we've completed all questions
    if st.session_state.current_question_index >= total_questions:
        # All questions completed - check if both users are done
        user1_guesses = get_user_guesses(game_id, user1_id)
        user2_guesses = get_user_guesses(game_id, user2_id)
        
        st.write(f"DEBUG: User1 guesses count: {len(user1_guesses)}")
        st.write(f"DEBUG: User2 guesses count: {len(user2_guesses)}")
        st.write(f"DEBUG: Total questions: {total_questions}")
        
        if len(user1_guesses) == total_questions and len(user2_guesses) == total_questions:
            # Both users completed - move to results phase
            from database import update_game_status
            update_game_status(game_id, "completed")
            st.session_state.current_question_index = 0  # Reset for results phase
            st.success("Both users completed all guesses! Moving to results phase.")
            st.rerun()
        else:
            st.success("✅ You completed all guesses! Waiting for your partner...")
            return
    
    # Get current question
    question = questions[st.session_state.current_question_index]
    question_id, question_text, options_json, created_at = question
    options = json.loads(options_json)
    
    st.write(f"**Question {st.session_state.current_question_index + 1}:** {question_text}")
    st.write("What do you think your partner chose?")
    
    # Check if already guessed
    existing_guess = next((guess[1] for guess in existing_guesses if guess[0] == question_id), None)
    default_index = existing_guess if existing_guess is not None and existing_guess < len(options) else 0
    
    selected_option = st.radio(
        "Make your guess:", 
        options, 
        key=f"guess_{question_id}_{current_user_id}",
        index=default_index
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Previous Question", disabled=st.session_state.current_question_index == 0):
            st.session_state.current_question_index -= 1
            st.rerun()
    
    with col2:
        if st.button("Next Question"):
            # Save guess
            option_index = options.index(selected_option)
            save_guess(game_id, current_user_id, question_id, option_index)
            
            # Move to next question
            if st.session_state.current_question_index < total_questions - 1:
                st.session_state.current_question_index += 1
                st.rerun()
            else:
                # All questions completed - check if both users are done
                user1_guesses = get_user_guesses(game_id, user1_id)
                user2_guesses = get_user_guesses(game_id, user2_id)
                
                if len(user1_guesses) == total_questions and len(user2_guesses) == total_questions:
                    from database import update_game_status
                    update_game_status(game_id, "completed")
                    st.session_state.current_question_index = 0  # Reset for results phase
                    st.success("Both users completed all guesses! Moving to results phase.")
                    st.rerun()
                else:
                    st.success("All guesses completed! Waiting for your partner...")
    
    # Progress bar
    progress = (st.session_state.current_question_index + 1) / total_questions
    st.progress(progress)
    st.write(f"Progress: {st.session_state.current_question_index + 1}/{total_questions} questions")

def show_results_phase(game_id, current_user_id, partner_id, user1_id, user2_id):
    """Display results for the completed game"""
    import streamlit as st
    from database import get_game_questions, get_user_answers, get_user_guesses
    
    st.subheader("Game Results!")
    
    # Get questions for this specific game (already filtered by batch)
    questions = get_game_questions(game_id)
    total_questions = len(questions)
    
    if total_questions == 0:
        st.error("No questions available for this batch!")
        return
    
    # Display batch information
    st.write(f"**Results for {total_questions} questions**")
    
    # Get answers and guesses
    question_ids = [q[0] for q in questions]
    user1_answers = {q_id: ans for q_id, ans in get_user_answers(game_id, user1_id) if q_id in question_ids}
    user2_answers = {q_id: ans for q_id, ans in get_user_answers(game_id, user2_id) if q_id in question_ids}
    user1_guesses = {q_id: guess for q_id, guess in get_user_guesses(game_id, user1_id) if q_id in question_ids}
    user2_guesses = {q_id: guess for q_id, guess in get_user_guesses(game_id, user2_id) if q_id in question_ids}
    
    # Debug info
    with st.expander("Debug Info - Results"):
        st.write(f"Total questions: {total_questions}")
        st.write(f"User1 answers: {len(user1_answers)}")
        st.write(f"User2 answers: {len(user2_answers)}")
        st.write(f"User1 guesses: {len(user1_guesses)}")
        st.write(f"User2 guesses: {len(user2_guesses)}")
        st.write(f"Question IDs: {question_ids}")
    
    # Calculate scores
    user1_correct_guesses = sum(1 for q_id, guess in user1_guesses.items() 
                               if user2_answers.get(q_id) == guess)
    user2_correct_guesses = sum(1 for q_id, guess in user2_guesses.items() 
                               if user1_answers.get(q_id) == guess)
    
    # Display scores
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Your Correct Guesses", user1_correct_guesses if current_user_id == user1_id else user2_correct_guesses)
    with col2:
        st.metric("Partner's Correct Guesses", user2_correct_guesses if current_user_id == user1_id else user1_correct_guesses)
    
    # Display detailed results
    for i, question in enumerate(questions):
        question_id, question_text, options_json, created_at = question
        options = json.loads(options_json)
        
        with st.expander(f"Question {i+1}: {question_text}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Your Answer:**")
                if current_user_id == user1_id:
                    user_answer = user1_answers.get(question_id)
                    user_guess = user1_guesses.get(question_id)
                    partner_answer = user2_answers.get(question_id)
                else:
                    user_answer = user2_answers.get(question_id)
                    user_guess = user2_guesses.get(question_id)
                    partner_answer = user1_answers.get(question_id)
                
                if user_answer is not None:
                    st.write(f"- You selected: **{options[user_answer]}**")
                    if user_guess is not None:
                        st.write(f"- You guessed partner would select: **{options[user_guess]}**")
                        if user_guess == partner_answer:
                            st.success("✓ Correct guess!")
                        else:
                            st.error(f"✗ Wrong! Partner selected: {options[partner_answer]}")
            
            with col2:
                st.write("**Partner's Answer:**")
                if partner_answer is not None:
                    st.write(f"- Partner selected: **{options[partner_answer]}**")
                    if current_user_id == user1_id:
                        partner_guess = user2_guesses.get(question_id)
                    else:
                        partner_guess = user1_guesses.get(question_id)
                    
                    if partner_guess is not None:
                        st.write(f"- Partner guessed you would select: **{options[partner_guess]}**")
                        if partner_guess == user_answer:
                            st.success("✓ Correct guess!")
                        else:
                            st.error(f"✗ Wrong! You selected: {options[user_answer]}")
    
    # Play Again button
    st.markdown("---")
    st.write("🎉 **Game Completed!**")
    
    if st.button("🔄 Play Again", key="play_again", type="primary"):
        st.session_state.current_game = None
        st.session_state.current_question_index = 0
        st.session_state.current_batch_index = 0
        st.session_state.user_answers = {}
        st.session_state.user_guesses = {}
        st.rerun()

def initialize_questions_if_empty():
    """Initialize sample questions if database is empty"""
    if len(get_all_questions()) == 0:
        load_sample_questions()

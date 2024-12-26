import streamlit as st

def display_ascii_art(art):
    """Displays ASCII art passed as a parameter."""
    st.text(art)

def game_intro():
    """Introduction to the game."""
    st.title("🎉 Virtual Date Adventure 🎉")
    st.subheader("Relive an unforgettable first date!")
    st.markdown("""
    Every choice you make shapes the story, so choose wisely. 
    Click the **Start Adventure** button to begin!
    """)
    if st.button("Start Adventure"):
        st.session_state.scene = 1

def make_choice(prompt, options):
    """
    Displays a prompt with multiple choice options and returns the player's choice.
    
    Parameters:
    - prompt: The question to ask the player.
    - options: A dictionary of valid options (e.g., {"1": "Option 1 text", "2": "Option 2 text"}).
    """
    st.write(prompt)
    choice = st.radio("Choose an option:", list(options.values()), key=f"scene_{st.session_state.scene}")
    selected_key = [k for k, v in options.items() if v == choice][0]
    if st.button("Submit Choice"):
        return selected_key
    return None

def game():
    """Main game function."""
    if "scene" not in st.session_state:
        st.session_state.scene = 0

    # Scene 0: Introduction
    if st.session_state.scene == 0:
        game_intro()

    # Scene 1: Arrival at the Restaurant
    elif st.session_state.scene == 1:
        prompt = "You walk into the restaurant and spot Eric sitting at a cozy table near the window. What do you do?"
        options = {
            "1": "Smile, wave and walk over to Eric.",
            "2": "Look at yourself with your camera to make sure you're ready, then compose yourself and head over confidently.",
            "3": "Surprise him by sneaking up quietly to the table."
        }
        choice = make_choice(prompt, options)
        if choice:
            st.write({
                "1": "Eric waves back, smiling warmly as you approach.",
                "2": "You take a deep breath, then walk over with poise. Eric smiles immensely!",
                "3": "He’s caught off guard but laughs, clearly charmed by your playful entrance and astonishing looks."
            }[choice])
            st.session_state.scene = 2

    # Scene 2: Breaking the Ice
    elif st.session_state.scene == 2:
        prompt = "The conversation starts easily. What topic do you bring up first?"
        options = {
            "1": "Ask him how his day has been so far.",
            "2": "Talk about the cozy ambiance of the restaurant.",
            "3": "Bring up that it's about time that we met up."
        }
        choice = make_choice(prompt, options)
        if choice:
            st.write({
                "1": "He shares a bit about his day, and the conversation flows naturally.",
                "2": "He agrees, pointing out the amazing smell of the food that's being cooked and the beautiful sight that's in front of him.",
                "3": "He agrees that it is about time and can't stop smiling. The mood becomes even more relaxed and fun."
            }[choice])
            st.session_state.scene = 3

    # Scene 3: The Dinner
    elif st.session_state.scene == 3:
        prompt = "As we order our food, talk, and then dinner arrives, the conversation deepens. What do you ask him about?"
        options = {
            "1": "His favorite thing that he has done on Christmas break.",
            "2": "A funny or embarrassing memory from his childhood or from his years in college.",
            "3": "What he’s looking forward to most this holiday season."
        }
        choice = make_choice(prompt, options)
        if choice:
            st.write({
                "1": "He shares a few heartwarming stories about family, and you find yourself smiling the whole time.",
                "2": "His story has you both laughing, making you realize that he's opening up to you.",
                "3": "His answer about what he wanted this holiday season reveals how much he values meaningful connections like the one he managed to get through tiktok, of all places."
            }[choice])
            st.session_state.scene = 4

    # Scene 4: The Gesture
    elif st.session_state.scene == 4:
        prompt = "As the evening winds down, he seems a little fidgety, like he’s planning something. What do you do?"
        options = {
            "1": "Playfully ask if he’s nervous about something.",
            "2": "Wait patiently, feeling curious to see what might happen next.",
            "3": "Lean in closer, noticing the glimmer of excitement in his brown eyes."
        }
        choice = make_choice(prompt, options)
        if choice:
            st.write({
                "1": "He laughs nervously and says, 'You’ll see soon enough!'",
                "2": "You wait, feeling the anticipation build as he reaches into his pocket.",
                "3": "He grins, clearly happy that you’re just as curious as he is."
            }[choice])
            st.session_state.scene = 5

    # Final Scene: The Big Reveal
    elif st.session_state.scene == 5:
        st.write("As the conversation pauses, he suddenly pulls something from his pocket.")
        st.write("With a warm smile, he holds it above you, and you look up to see...")
        mistletoe_art = """
           ____  
         {0  0}  
          \__/   
           |||   
          /   \  
         |_____|  
        """
        display_ascii_art(mistletoe_art)
        st.write("A mistletoe, dangling playfully above you.")
        st.write("Your cheeks flush as you meet his gaze, and you both share a smile.")
        st.write("He leans closer, and the moment becomes magical. **The End.**")

# Run the game
if __name__ == "__main__":
    game()

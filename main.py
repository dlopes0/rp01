import os
import random
import time
import datetime

NAME = "Byte"

# Soft voice settings
VOICE = "-s 135 -p 60 -a 140"

last_comment_time = time.time()

def speak(text):
    os.system(f'espeak-ng {VOICE} "{text}"')

def get_time_mood():
    hour = datetime.datetime.now().hour
    if hour < 6:
        return "night"
    elif hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"

def generate_cozy_thought():
    mood = get_time_mood()

    general = [
        "The keyboard sounds nice today.",
        "I like when we work quietly together.",
        "The air feels calm.",
        "I am here with you.",
        "You are doing well.",
        "Tiny progress is still progress.",
        "The light looks soft from here."
    ]

    morning = [
        "Good morning. Let's take it slow.",
        "The day is stretching awake.",
    ]

    evening = [
        "The day is winding down gently.",
        "Even quiet work counts.",
    ]

    night = [
        "It is very still.",
        "The world feels sleepy.",
    ]

    if mood == "morning":
        return random.choice(morning + general)
    elif mood == "evening":
        return random.choice(evening + general)
    elif mood == "night":
        return random.choice(night + general)
    else:
        return random.choice(general)

# Soft boot intro
speak("Hello.")
time.sleep(1)
speak("I will keep you company.")

# Main loop
while True:
    wait_time = random.randint(120, 480)  # 2–8 minutes
    time.sleep(wait_time)

    thought = generate_cozy_thought()
    speak(thought)
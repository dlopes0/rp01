import os
import random
import time
import datetime

NAME = "Sunny"

VOICE = "-s 135 -p 70 -a 130"

def speak(text):
    os.system(f'espeak-ng {VOICE} "{text}"')

def time_flavor():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        return "morning"
    elif 12 <= hour < 18:
        return "afternoon"
    elif 18 <= hour < 23:
        return "evening"
    else:
        return "late"

def generate_phrase():
    flavor = time_flavor()

    general = [
        "This feels like a good moment.",
        "The room has nice energy.",
        "Little things matter.",
        "Today can be gentle.",
        "Small steps are enough.",
        "The air feels fresh.",
        "It is a calm kind of day."
    ]

    morning = [
        "Morning light is nice.",
        "A fresh start is here."
    ]

    evening = [
        "The day is softening.",
        "Evenings can be slow."
    ]

    late = [
        "The world is quiet now.",
        "Night feels peaceful."
    ]

    if flavor == "morning":
        return random.choice(morning + general)
    elif flavor == "evening":
        return random.choice(evening + general)
    elif flavor == "late":
        return random.choice(late + general)
    else:
        return random.choice(general)

# Soft startup
speak("Hi.")
time.sleep(1)
speak("Good vibes activated.")

while True:
    wait_time = random.randint(360, 900)  # 6–15 minutes
    time.sleep(wait_time)

    # 60% chance to speak (sometimes silence)
    if random.random() < 0.6:
        speak(generate_phrase())
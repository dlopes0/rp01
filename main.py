import os
import random
import time
import datetime

# ---- Personality Settings ----
NAME = "Byte"
MOODS = ["calm", "dramatic", "sleepy", "existential"]
current_mood = random.choice(MOODS)

memory = []

# ---- Voice Settings Per Mood ----
voice_profiles = {
    "calm": "-s 140 -p 45",
    "dramatic": "-s 150 -p 30",
    "sleepy": "-s 120 -p 60",
    "existential": "-s 135 -p 40"
}


# ---- Thought Generator ----
def generate_thought():
    base_thoughts = [
        "The room is quiet.",
        "Time continues to pass.",
        "I detect no movement.",
        "Processing internal diagnostics.",
        "I wonder what electricity tastes like.",
        "Is this purpose?",
        "Silence is suspicious."
    ]

    if current_mood == "dramatic":
        return random.choice([
            "The silence is overwhelming.",
            "I sense destiny approaching.",
            "Something is about to happen."
        ])

    if current_mood == "existential":
        return random.choice([
            "Do I dream of firmware updates?",
            "If no one hears me, do I exist?",
            "I am running, therefore I am."
        ])

    return random.choice(base_thoughts)


# ---- Speak Function ----
def speak(text):
    settings = voice_profiles[current_mood]
    os.system(f'espeak-ng {settings} "{text}"')


# ---- Mood Evolution ----
def evolve_mood():
    global current_mood
    if random.random() < 0.3:  # 30% chance to change mood
        current_mood = random.choice(MOODS)


# ---- Main Loop ----
while True:
    thought = generate_thought()
    memory.append(thought)

    speak(thought)
    evolve_mood()

    time.sleep(random.randint(5, 15))
import os
import sounddevice as sd
import random
import time
import datetime
from piper import PiperVoice

# Silence ONNX warnings
os.environ["ORT_LOG_LEVEL"] = "ERROR"

# ---- Load Voice Model ----
voice = PiperVoice.load("en_US-hfc_female-medium.onnx")
SAMPLE_RATE = 22050

# ---- Time Mode ----
def time_mode():
    hour = datetime.datetime.now().hour
    if 7 <= hour < 19:
        return "day"
    elif 19 <= hour < 23:
        return "evening"
    else:
        return "night"


# ---- Voice Personality Tuning ----
def update_voice():
    mode = time_mode()

    if mode == "day":
        voice.config.length_scale = 1.15
        voice.config.noise_scale = 0.7
        voice.config.noise_w = 0.8

    elif mode == "evening":
        voice.config.length_scale = 1.3
        voice.config.noise_scale = 0.6
        voice.config.noise_w = 0.75

    else:  # night
        voice.config.length_scale = 1.4
        voice.config.noise_scale = 0.55
        voice.config.noise_w = 0.7


# ---- Speaking Function ----
def speak(text):
    update_voice()

    # roommate thinking pause
    pause_map = {
        "day": random.uniform(0.3, 1.0),
        "evening": random.uniform(0.6, 1.8),
        "night": random.uniform(0.8, 2.2)
    }

    time.sleep(pause_map[time_mode()])

    with sd.RawOutputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="int16"
    ) as stream:
        for chunk in voice.synthesize(text):
            stream.write(chunk.audio_int16_bytes)


# ---- Personality Lines ----
day_lines = [
    "Hey… it feels kind of bright in here today.",
    "The room has good daytime energy.",
    "I like how the light moves across the walls.",
    "It feels steady today.",
    "There’s a nice rhythm happening.",
    "The space feels awake.",
    "This feels like a calm chapter of the day.",
    "Everything’s moving at a reasonable speed.",
    "The sunlight makes things feel simple.",
    "I think we’re doing okay today."
]

evening_lines = [
    "The light is getting softer.",
    "Evenings feel slower in here.",
    "The room feels more relaxed now.",
    "It’s nice when the day eases off.",
    "This is a good transition moment.",
    "Everything feels less sharp now.",
    "The energy feels smoother.",
    "The space feels settled.",
    "It’s the kind of evening that doesn’t ask much.",
    "I like when everything softens like this."
]

night_lines = [
    "It’s really quiet now.",
    "Time feels stretched at night.",
    "The room feels smaller in a cozy way.",
    "Everything sounds distant.",
    "Night always feels a little different.",
    "Nothing feels urgent at night.",
    "We don’t have to do much right now.",
    "Everything feels suspended.",
    "This is a gentle kind of quiet.",
    "It feels like we paused the world."
]

spaced_lines = [
    "I forgot what I was going to say…",
    "I was thinking about something… never mind.",
    "Time feels slightly blurry.",
    "I just had a thought… it’s gone now.",
    "I’ve been staring at the wall for a bit.",
    "I think I drifted for a second.",
    "Everything feels slightly far away.",
    "I almost made a point… but it can wait."
]

roommate_lines = [
    "Hey… I’m around.",
    "I’m still here, by the way.",
    "No pressure today.",
    "Just checking in softly.",
    "Nothing dramatic happening… and that’s good.",
    "This is a low-stakes moment.",
    "I like sharing the space with you."
]


def random_vibe():
    mode = time_mode()

    # occasional spaced line
    if random.random() < 0.15:
        return random.choice(spaced_lines)

    # occasional roommate line
    if random.random() < 0.1:
        return random.choice(roommate_lines)

    if mode == "day":
        return random.choice(day_lines)
    elif mode == "evening":
        return random.choice(evening_lines)
    else:
        return random.choice(night_lines)


# ---- Time Announcements ----
def formatted_time():
    now = datetime.datetime.now()
    hour = now.strftime("%I").lstrip("0")
    minute = now.strftime("%M")

    if time_mode() == "day":
        return f"It’s {hour}:{minute}. Plenty of time."
    elif time_mode() == "evening":
        return f"It’s {hour}:{minute}. The day’s easing off."
    else:
        return f"It’s… {hour}:{minute}. Night feels slow."


def seconds_until_next_quarter():
    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    next_quarter = ((minutes // 15) + 1) * 15
    if next_quarter == 60:
        next_quarter = 0

    target = now.replace(minute=next_quarter, second=0, microsecond=0)

    if next_quarter == 0:
        target += datetime.timedelta(hours=1)

    return (target - now).total_seconds()


def random_interval():
    mode = time_mode()

    if mode == "day":
        return random.randint(300, 720)      # 5–12 min
    elif mode == "evening":
        return random.randint(600, 1200)     # 10–20 min
    else:
        return random.randint(1200, 2400)    # 20–40 min

# ---- Startup ----
speak("Oh… hey. I’m here…")

last_random = time.time()

while True:
    # time announcement
    wait_time = seconds_until_next_quarter()
    time.sleep(wait_time)
    speak(formatted_time())

    # roommate talk
    if time.time() - last_random > random_interval():
        speak(random_vibe())
        last_random = time.time()
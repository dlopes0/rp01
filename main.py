import os
import time
import datetime
import random

VOICE = "-s 135 -p 70 -a 125"

def speak(text):
    os.system(f'espeak-ng {VOICE} "{text}"')

def formatted_time():
    now = datetime.datetime.now()
    hour = now.strftime("%I").lstrip("0")
    minute = now.strftime("%M")
    period = now.strftime("%p")

    if minute == "00":
        return f"It is {hour} {period}."
    else:
        return f"It is {hour} {minute} {period}."

def random_phrase():
    phrases = [
        "The room feels nice.",
        "This is a calm moment.",
        "Small things matter.",
        "It is a good kind of quiet.",
        "The air feels fresh.",
        "Today can be gentle.",
        "Everything is moving at its own pace.",
        "Light is shifting softly.",
        "This moment is enough."
    ]
    return random.choice(phrases)

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

# Startup
speak("Bedroom mode active.")

while True:
    wait_time = seconds_until_next_quarter()

    # Random vibe window between now and next quarter
    random_offset = random.randint(60, int(wait_time - 10)) if wait_time > 70 else None

    start_time = time.time()

    while time.time() - start_time < wait_time:
        elapsed = time.time() - start_time

        # Speak random phrase once before next time announcement
        if random_offset and elapsed >= random_offset:
            speak(random_phrase())
            random_offset = None  # only once per cycle

        time.sleep(1)

    # Announce exact time
    speak(formatted_time())
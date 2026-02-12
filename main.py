import os
import time
import datetime
import random

VOICE = "-v pt -s 95 -p 80 -a 110"

def speak(text):
    os.system(f'espeak-ng {VOICE} "{text}"')

def formatted_time():
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute

    if minute == 0:
        return f"São {hour} horas."
    else:
        return f"São {hour} e {minute}."

def random_phrase():
    phrases = [
        "O quarto está com uma energia boa.",
        "Este é um momento tranquilo.",
        "As pequenas coisas importam.",
        "O silêncio é confortável.",
        "O ar parece leve.",
        "Hoje pode ser gentil.",
        "Tudo está no seu próprio ritmo.",
        "A luz está mudando devagar.",
        "Este momento já é suficiente."
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

# Inicialização
speak("Modo quarto ativado.")

while True:
    wait_time = seconds_until_next_quarter()

    # Momento aleatório antes do próximo anúncio de hora
    random_offset = random.randint(60, int(wait_time - 10)) if wait_time > 70 else None

    start_time = time.time()

    while time.time() - start_time < wait_time:
        elapsed = time.time() - start_time

        if random_offset and elapsed >= random_offset:
            speak(random_phrase())
            random_offset = None

        time.sleep(1)

    # Anuncia hora exata
    speak(formatted_time())
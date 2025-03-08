from config import WAKE_WORD
from core.speech_hander import listen

def wake_word_detected():
    command = listen()
    if WAKE_WORD in command:
        return True
    return False
import datetime

from core.speech_hander import speak

def get_time():
    now = datetime.datetime.now()
    speak(f"The time is {now.strftime('%H:%M:%S')}")
import commands

def handle_action(intent, command):
    if intent == 'time':
        time.get_time()
    elif intent == 'weather':
        get_weather(command)
    elif intent == 'exit':
        return False
    elif intent == 'unknown':
        from core.speech_hander import speak
        speak('Sorry, I did not get that')
    return True
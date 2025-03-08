def parse_intent(command):
    if "time" in command:
        return "time"
    elif "weather" in command:
        return "weather"
    elif "exit" in command:
        return "exit"
    else:
        return "unknown"
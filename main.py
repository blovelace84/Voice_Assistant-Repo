from core import speech_hander as speech_handler, nlu_handler, action_handler, wake_word

if __name__ == "__main__":
    while True:
        if wake_word.wake_word_detected():
            command = speech_handler.listen()
            if command:
                intent = nlu_handler.parse_intent(command)
                if not action_handler.handle_action(intent, command):
                    break

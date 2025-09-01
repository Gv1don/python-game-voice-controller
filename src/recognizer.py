import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_command():
    """Слушает голос и возвращает текст команды (строку)"""
    with sr.Microphone() as source:
        print("Слушаю команду...")
        audio = recognizer.listen(source, phrase_time_limit=3)
        try:
            text = recognizer.recognize_google(audio, language="ru-RU")
            text = text.lower()
            print(f"Распознано: {text}")
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError as e:
            print(f"Ошибка сервиса: {e}")
            return None

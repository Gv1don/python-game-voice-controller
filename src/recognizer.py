import sounddevice as sd
import numpy as np
import speech_recognition as sr

recognizer = sr.Recognizer()
fs = 44100

def listen_command(duration=3):
    """
    Слушает голос и возвращает текст команды (строку) с помощью sounddevice.
    duration — длительность записи в секундах.
    """
    print("Слушаю команду...")
    try:
        audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()

        audio = sr.AudioData(audio_data.tobytes(), fs, 2)

        text = recognizer.recognize_google(audio, language="ru-RU")
        text = text.lower()
        print(f"Распознано: {text}")
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(f"Ошибка сервиса: {e}")
        return None
    except Exception as e:
        print(f"Ошибка записи аудио: {e}")
        return None

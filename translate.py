import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os

# Initialize components
r = sr.Recognizer()
translator = Translator()

print("--- Voice Translator Started (Say 'exit' to stop) ---")

while True:
    with sr.Microphone() as source:
        # Adjust for ambient noise for better accuracy
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("\nListening...")
        audio = r.listen(source)
        
        try:
            # 1. Speech to Text
            speech_text = r.recognize_google(audio)
            print(f"You said: {speech_text}")
            
            if speech_text.lower() == "exit":
                print("Goodbye!")
                break
                
            # 2. Translation
            # Note: 'dest' is used in googletrans instead of 'lang_tgt'
            translation = translator.translate(speech_text, dest='fr')
            translated_text = translation.text
            print(f"French: {translated_text}")

            # 3. Text to Speech
            voice = gTTS(translated_text, lang='fr')
            filename = "temp_voice.mp3"
            voice.save(filename)
            
            # 4. Playback
            playsound(filename)
            os.remove(filename)

        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

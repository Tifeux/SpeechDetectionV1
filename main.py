import speech_recognition as sr
import pyttsx3
import webbrowser
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Écoute...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio, language="fr-FR")
        print("Vous avez dit :", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Je n'ai pas compris.")
        return ""
    except sr.RequestError:
        print("Erreur avec le service de reconnaissance vocale.")
        return ""

def execute_command(command):
    if "ouvre" in command:
        filename = command.replace("ouvre", "").strip()
        try:
            os.startfile(filename)
            speak(f"J'ouvre {filename}")
        except Exception as e:
            print("Erreur :", e)
            speak("Je ne peux pas ouvrir ce fichier.")
    elif "cherche" in command:
        query = command.replace("cherche", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Voici les résultats pour {query}")
    else:
        speak("Je ne connais pas cette commande.")

if __name__ == "__main__":
    speak("Bonjour, que puis-je faire pour vous ?")
    while True:
        command = recognize_speech()
        if "arrête" in command:
            speak("Au revoir !")
            break
        elif command:
            execute_command(command)

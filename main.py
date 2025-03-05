import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import pyttsx3
import webbrowser

class SpeechDectection:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeechDetectionV1")
        self.root.geometry("500x400")
        self.root.minsize(400, 300)
        
        # Styles
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5)
        style.configure("TLabel", font=("Arial", 14))
        
        # Interface
        self.label = ttk.Label(root, text="Assistant Vocal", anchor="center")
        self.label.pack(pady=10)
        
        self.text_output = tk.Text(root, height=10, wrap="word", state="disabled")
        self.text_output.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        self.listen_button = ttk.Button(root, text="🎤 Parler", command=self.listen)
        self.listen_button.pack(pady=10)
        
        # Initialisation TTS
        self.engine = pyttsx3.init()
        
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            self.update_text("Parlez maintenant...")
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio, language="fr-FR").lower()
                self.update_text(f"Vous avez dit : {command}")
                self.process_command(command)
            except sr.UnknownValueError:
                self.update_text("Je n'ai pas compris.")
            except sr.RequestError:
                self.update_text("Erreur de connexion.")
    
    def process_command(self, command):
        if "recherche" in command:
            query = command.replace("recherche", "").strip()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            self.speak(f"Voici les résultats pour {query}.")
        elif "bonjour" in command:
            self.update_text("Bonjour à vous !")
            self.speak("Bonjour à vous !")
        else:
            self.update_text("Commande non reconnue.")
            self.speak("Commande non reconnue.")
    
    def update_text(self, message):
        self.text_output.config(state="normal")
        self.text_output.insert(tk.END, message + "\n")
        self.text_output.config(state="disabled")
        self.text_output.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistant(root)
    root.mainloop()

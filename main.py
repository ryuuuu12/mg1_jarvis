import speech_recognition as sr
import webbrowser
import pyttsx3
import music_libray


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open x" in c.lower():
        webbrowser.open("https://X.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link =  music_libray.music[song]
        webbrowser.open(link)
    pass
    

if __name__  == "__main__":
    speak("Initializing Jarvis... ")
    while True:
        # Listen for the wake word jarvis
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        
        

        # recognize speech using Sphinx
        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("jarvis active")
                    audio = r.listen(source, timeout=2)
                    word = r.recognize_google(audio)
                    processcommand(word)
                
                
                
        except Exception as e:
            print(" Error; {0}".format(e))
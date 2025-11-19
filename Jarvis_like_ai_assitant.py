# install speech recoginition 
# use webbrowser
# use pyttsx3
# use setuptools
# use  

import speech_recognition as sr
import webbrowser
import pyttsx3


r = sr.Recognizer() 
engine = pyttsx3.init()

def speak(text):
    """Function to make the assistant speak"""
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    """Function to execute the final command"""
    print(f"Executing command: {c}")
    
   
    if "open google" in c:
        speak("Opening Google.")
        webbrowser.open("http://www.google.com")
    elif "open youtube" in c:
        speak("opening youtube")
        webbrowser.open("http://www.youtube.com")
    elif "open reddit" in c:
        speak("opening reddit")
        webbrowser.open("http://www.reddit.com")
   
    elif "stop" in c:
        speak("Goodbye!")
        exit()
    else:
        speak("Command received but not recognized.")
    
if __name__ == "__main__":
    speak("initializing Jarvis...")
    print("Recognizer initialized.")
    
    while True:
        
        print("\n--- Waiting for Wake Word ---")
        
        try:
            with sr.Microphone() as source:
                
                print("Listening for wake word: ")
                
                audio = r.listen(source, timeout=2, phrase_time_limit=1.5)
            
            
            word = r.recognize_google(audio).lower() 
            print(f"Recognized (wake attempt): {word}")
            
            
            if "jarvis" in word:
                speak("Yes? How can I help you?")
                
              
                
                with sr.Microphone() as source: 
                    print("Jarvis now listening for command...")
                    
                    
                    audio = r.listen(source, phrase_time_limit=5) 
                    
                    
                    command = r.recognize_google(audio).lower()
                    process_command(command)
            
        except sr.UnknownValueError:
           
            print("No recognizable speech detected.")
            
        except sr.WaitTimeoutError:
            
            print("Timeout. No sound detected during listening phase.")
            
        except Exception as e:
            
            print(f"An unexpected error occurred: {e}")
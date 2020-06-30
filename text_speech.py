
import pyaudio
import pyttsx3 

def TextToSpeech(Data):
    engine = pyttsx3.init()
    engine.say(Data)
    engine.runAndWait() 
    

print("tye something")
user_input=input()
TextToSpeech(user_input)
   
   
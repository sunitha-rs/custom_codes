

import speech_recognition as sr     # import the library
import pyaudio
import pyttsx3 
import inflect
from chatterbot import ChatBot    
from chatterbot.trainers import ChatterBotCorpusTrainer 

chatterbot = ChatBot("Training Example") 
trainer =  ChatterBotCorpusTrainer(chatterbot) 
trainer.train("chatterbot.corpus.english.my_chatpot") 


#user_input = input()  
#response = chatterbot.get_response(user_input)
#response = chatterbot.get_response('What is your name?')
#print(response) 




d={"BED UP":1,"BED DOWN":2,"LIGHT ON":3,"LIGHT OFF":4,
    "FAN ON":5,"FAN OFF":6,"MOOD RED":7,"MOOD GREEN":8,
    "BLINDS OPEN":9,"BLINDS CLOSE":10,"EXIT":11}

print(d)

print(d.keys())
print(d.values())  




def TextToSpeech(Data):
    engine = pyttsx3.init()
    engine.say(Data)
    engine.runAndWait()  

def numbertostr(Data):
    p = inflect.engine()
    words = p.number_to_words(Data)
    #p.number_to_words(Data)

# Prints “one thousand, two hundred and thirty-four”
    print(words)

def stringComp(word):
    if str(word) == "too":
        return 2
    if str(word) == "tow":
        return 2
    if str(word) == "tu":
        return 2
    if str(word) == "kyon":
        return 2    
    if str(word) == "to":
        return 2
    if str(word) == "tree":
        return 3
    if str(word) == "free":
        return 2
    if str(word) == "v":
        return 5
    if str(word) == "Vee":
        return 5 
    return word
    

r = sr.Recognizer() 
#engine = pyttsx3.init()                # initialize recognizer
while True:
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)     # listen to the source
        try:
            text = r.recognize_google(audio)             # use recognizer to convert our audio into text part.
            print("** String Compared ** ",stringComp(text))
            text = text.upper()
            print("You said : {}".format(text))
             
  
            if "ALEXA" in text:
                while True:
                    print("\n")
                    print("alexa is working and contains the predefined commands")
                    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
                        #TextToSpeech("please say some thing :")
                        print("please say some thing :")
                        
                        r.adjust_for_ambient_noise(source,duration=0.2)
                        audio = r.listen(source)     # listen to the source
                        
                       
                        try:
                            text = r.recognize_google(audio)    # use recognizer to convert our audio into text part.
                            text = text.upper()       
                            print("You said : {}".format(text))
                            
                            
                            #response = chatterbot.get_response(text)
                            #response = chatterbot.get_response('What is your name?')
                            #print(response) 

                            
                            fetch=d.get(text,None)
                            fetched_command = "command not found and try again"
                            if fetch:                                
                               fetched_command = "Command recognized: "+str(fetch)
                              
                               print(fetched_command)
                               TextToSpeech(fetched_command)
                            
                               break
                            else:
                                response = chatterbot.get_response(text)
                            #response = chatterbot.get_response('What is your name?')
                                print(response)
                                TextToSpeech(response)
                                
                                

                        except:
                            print("command not identified")

            TextToSpeech(text)
            numbertostr(text)
            
        except:
            print("Sorry could not recognize your voice")    # In case of voice not recognized  clearlyw
        
 
        

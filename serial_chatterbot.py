 

import speech_recognition as sr     # import the library
import pyaudio
import pyttsx3 
import inflect
from chatterbot import ChatBot    
from chatterbot.trainers import ChatterBotCorpusTrainer 
import serial

chatterbot = ChatBot("Training Example") 
trainer =  ChatterBotCorpusTrainer(chatterbot) 
trainer.train("chatterbot.corpus.english.my_chatpot") 

serialPort =serial.Serial(port = "COM3", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

neg_list = ["EXIT","NOT","DON'T"]






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
    

CurrentDataPacket="hii, bluetooth working" # sending value to the terminal

print(serialPort.write(str.encode(CurrentDataPacket))) # GETTING OUTPUT FROM THE SERIAL PORT.



r = sr.Recognizer() 
#engine = pyttsx3.init()                # initialize recognizer
while True:
    with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
        print("Speak Anything :")  # simple hello
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)     # listen to the source
        try:
            text = r.recognize_google(audio)             # use recognizer to convert our audio into text part.
            print("** String Compared ** ",stringComp(text))
            text = text.upper() # Hello
            print("You said : {}".format(text))

            if "ALEXA" in text:       # alexa enter the loop  # alexa what is your name
                actual_text = text    # alexa enter the loop  # alexa what is your name
                split_text = set(text.split(" "))  # ["alexa","enter","the","loop"]  # ["alexa","what","is","your","name"]
                hold = list(split_text-set(neg_list))  #["alexa","enter","the","loop"] # ["alexa","what","is","your","name"]
                if  len(split_text)!=len(hold):        #                               
                     pass
                else:                                     # if length of the list set is equal then enters the else part
                    main_text = actual_text.replace("ALEXA","")   #                # what is your name
                    if main_text:
                       # CurrentDataPacket = main_text
                        main_response = chatterbot.get_response(main_text)#           # anything you want to call me
                        print("\n")
                        print(serialPort.write(str.encode(str(main_response)))) # GETTING OUTPUT FROM THE SERIAL PORT.
                        print(main_response)                                          # anything you want to call me
                        TextToSpeech(main_response)                                   # anything you want to call me
                    while True:                                                       # always true
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
                                actual_text = text
                                split_text = set( text.split(" ") )                               
                                hold = list(split_text-set(neg_list))
                                if  len(split_text)!=len(hold):
                                    break                      
                                text = actual_text.replace("ALEXA","")
                                fetch=d.get(text,None)
                                fetched_command = "command not found and try again"
                                if fetch:                                
                                    fetched_command = "Command recognized: "+str(fetch)
                              
                                    print(fetched_command)
                                    TextToSpeech(fetched_command)
                                    break
                                else:
                                    random_response = chatterbot.get_response(text)
                            #response = chatterbot.get_response('What is your name?')
                                    print(random_response)
                                    print("\n")
                                    print(serialPort.write(str.encode(str(random_response))))
                                    
                                    TextToSpeech(random_response)
                                
                                

                            except:
                                print("command not identified")

            TextToSpeech(text) # says Hello
            numbertostr(text)   # zero
            
        except Exception as e:
            print("ERROR TRY 1: ",e)
            print("Sorry could not recognize your voice")    # In case of voice not recognized  clearlyw
        
 
        
#note: working process

#1. speak something- hello, just speech synthesis
#2. allexa - just it will come in to the loop 
# if i say - hello hello hello alexa ,it will come into the loop and start conversation.

 
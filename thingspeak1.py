 

import speech_recognition as sr     # import the library
import pyaudio
import pyttsx3 
import inflect
from chatterbot import ChatBot    
from chatterbot.trainers import ChatterBotCorpusTrainer 
import serial
import re

import requests


chatterbot = ChatBot("Training Example") 
trainer =  ChatterBotCorpusTrainer(chatterbot) 
trainer.train("chatterbot.corpus.english.my_chatpot") 

serialPort =serial.Serial(port = "COM3", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

neg_list = ["EXIT","NOT","DON'T"]

entity=["FAN","WEATHER"]
operation=["INCREASE","DECREASE","SET","TURN ON","TURN OFF","ON","OFF"]





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
    

def thingspeak(entity,value):

    read_payload = {'results':2}
    read_url = "https://api.thingspeak.com/channels/1093982/feeds.json?results=2"
    try:
        response = requests.get(read_url)
        result = response.json()
        feeds = result['feeds']
        for i in feeds:
            print("fan=",i['field1'],"weather=",i['field2'])
    except Exception as e:
        print(e)
    
    #fan=input("write the fan value into the thingspeak")
    #weather=input("write the weather value into the thingspeak")
    field_ref = {"fan":"field1","weather":"field2"}
    write_payload = {'api_key':"VTZZCT7D0QJ64XQK"}
    change_field = field_ref.get(entity[0].lower(),False)
    if not change_field:
        print("ENTITY NOT FOUND")
        return
    write_payload[change_field] = value    
    # write_url = "https://api.thingspeak.com/update?api_key=VTZZCT7D0QJ64XQK&field1=0"
    write_url = "https://api.thingspeak.com/update"
    print(write_payload)
    try:
        response = requests.get(write_url,params=write_payload)
        print(response.json())
    except Exception as e:
        print(e)    
'''
def thingspeak_fan(num):

    read_payload = {'results':2}
    read_url = "https://api.thingspeak.com/channels/1093982/feeds.json?results=2"



    try:
        response = requests.get(read_url)
        result = response.json()
        feeds = result['feeds']
        for i in feeds:
            print("fan=",i['field1'])
    except Exception as e:
        print(e)
    
    #fan=input("write the fan value into the thingspeak")
   #weather=input("write the weather value into the thingspeak")

    
    write_payload = {'api_key':"VTZZCT7D0QJ64XQK",'field1':num}
    write_url = "https://api.thingspeak.com/update?api_key=VTZZCT7D0QJ64XQK&field1=0"



    try:
        response = requests.get(write_url,params=write_payload)
        print(response.json())
    except Exception as e:
        print(e)    
'''


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
            text = text.upper() # Hello
            print("You said : {}".format(text))

            if "LOCAL ALEXA" in text:       # alexa enter the loop  # alexa what is your name
                actual_text = text    # alexa enter the loop  # alexa what is your name
                split_text = set(text.split(" "))  # ["alexa","enter","the","loop"]  # ["alexa","what","is","your","name"]
                for x in split_text:
                    try:
                        if int (x) > 0: print (x)
                    except: 
                        continue

                    #if entity in split_text and "SPEED" in split_text and x in actual_text:
                
                     #   thingspeak()
                    #tgentity=list(split_text - set(entity))
                    #if len(split_text)!=len(tgentity):
                     #   pass    
                    
                    #tgoperation=list(split_text - set(operation))
                    #if len(split_text)!=len(tgoperation):
                     #   pass

                    #thingspeak(tgentity,tgoperation,x)    
                #for i in entity:
                    #for j in operation:
                        #thingspeak(entity,operation,x)    



                hold = list(split_text-set(neg_list))  #["alexa","enter","the","loop"] # ["alexa","what","is","your","name"]
                if  len(split_text)!=len(hold):        #                               
                     pass
                else:                                     # if length of the list set is equal then enters the else part
                    main_text = actual_text.replace("LOCAL ALEXA","")                  # what is your name
                    if main_text:

                        main_response = chatterbot.get_response(main_text)          # anything you want to call me
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
                                

                    #if entity in split_text and "SPEED" in split_text and x in actual_text:
                
                     #   thingspeak()
                                thingspeak_flag = False
                                tgentity=list(split_text - set(entity))
                                if len(split_text)!=len(tgentity):                                    
                                    # tgoperation=list(split_text - set(operation))
                                    # if len(split_text)!=len(tgoperation):
                                    for x in split_text:
                                        try:
                                            print(int(x))
                                            entity_found = list(split_text - set(tgentity))
                                            # op_found = list(split_text - set(tgoperation))
                                            thingspeak(entity_found,x)    
                                            thingspeak_flag = True
                                        except: 
                                            pass
                                if thingspeak_flag:
                                    break                
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
#2. local allexa - just it will come in to the loop 
#3.local allexa what is your name
#4 set fan to 70


 
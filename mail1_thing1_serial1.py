import smtplib 
from email.message import EmailMessage
import xlrd
from xlrd import open_workbook
import os
import re
import requests
import serial



class Justmail:
    def __init__(self):
        pass
    

    def mail(self,message=None):
        
        msg = EmailMessage()
        
        user_from=input("sender mailid\n")
        user_to=input("receiver mail.id\n")
        user_sub=input("message subject\n")
        if not message:
            user_message=input("write the message\n")
        else:
            user_message = message

        msg['From'] = user_from
        msg['To'] = user_to
        msg['Subject'] =user_sub 
        msg.set_content(user_message)
        # Send the message via our own SMTP server.
        print("\nAre you sure you want to send this mail? (yes/no) ")
        user_inputyesorno = input()
                        
        if user_inputyesorno =="no" or user_inputyesorno =="NO":
            print("\n processing mail has been cancelled")
            return
        elif user_inputyesorno == "yes" or user_inputyesorno == "YES": 
            print("\n_________________________")
        
        try:
            
            server = smtplib.SMTP_SSL('smtp.gmail.com',465)
            server.login("sunithareynold@gmail.com", "dolly@doss123")
            server.send_message(msg)
            server.quit()
            print("\nEmail sent successfully.")

        except Exception as e:
            print(e)
            pass    


    def thingspeak(self):
        
        light_fan_status={"ON":1,"OFF":0}
        read_payload = {'results':2}
        read_url = "https://api.thingspeak.com/channels/1098917/feeds.json?api_key=OQY7RQXDXMC51232&results=2"
            
        try:
            response = requests.get(read_url)
            result = response.json()
            feeds = result['feeds']
            for i in feeds:
                print("light=",i['field1'],"fan=",i['field2'],"fan_speed=",i['field3'],"temperature=",i['field4'])
        except Exception as e:
            print(e)
    
        light=input("write the light status(on or off) value into the thingspeak")
        light_switch=light_fan_status.get(light.upper(),0)
        fan=input("write the fan status(on or off) value into the thingspeak")
        fan_switch=light_fan_status.get(fan.upper(),0)
        fan_speed=input("write the fan speed value into the thingspeak")
        temperature=input("write the temperature value into the thingspeak")

    
        write_payload = {'api_key':"6OZ715PMNAC6MRWN",'field1':light_switch,'field2':fan_switch,'field3':fan_speed,'field4':temperature}
        write_url = "https://api.thingspeak.com/update?api_key=6OZ715PMNAC6MRWN&field1=0"

        try:
            response = requests.get(write_url,params=write_payload)
            print(response.json())
        except Exception as e:
            print(e)    

        return {"light":light,
                "fan":fan,
                "fan_speed":fan_speed,
                "temperature":temperature}


    def serial_port(self,ts_reading):
        serialPort =serial.Serial(port = "COM3", baudrate=9600,bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
        CurrentDataPacket="bluetooth is working"
        print(serialPort.write(str.encode(CurrentDataPacket))) # GETTING OUTPUT FROM THE SERIAL PORT.
        str_readings = ""
        for k,val in ts_reading.items():
            str_readings += k + " - " + str(val)+"\n"
        print(serialPort.write(str.encode(str_readings)))
        return str_readings


obj=Justmail()
obj.mail()
ts_reading=obj.thingspeak()
sr_reading=obj.serial_port(ts_reading)
print("sr_reading:",sr_reading)
 
obj.mail(message=sr_reading)




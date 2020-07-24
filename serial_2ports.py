

import serial
       

serialPort1 =serial.Serial(port = "COM3", baudrate=9600,bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)
serialPort2 =serial.Serial(port = "COM12", baudrate=9600,bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)

print(serialPort2.name)
print(serialPort1.name)

while True:
	CurrentDataPacket=input("write some thing\n\r")
	write1=serialPort1.write(str.encode(CurrentDataPacket))# displyed on moboile as dolly
	#read1=serialPort1.readlines() #b'dolly
	#print(read1)
	
	write2=serialPort2.write(str.encode(CurrentDataPacket))#dolly
	read2=serialPort2.readlines()
	print("reading in port_2 : ",read2)




'''
	
import serial
       

serialPort1 =serial.Serial(port = "COM3", baudrate=9600,bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)
#serialPort2 =serial.Serial(port = "COM12", baudrate=9600,bytesize=8, timeout=10, stopbits=serial.STOPBITS_ONE)

print(serialPort1.name)
#print(serialPort2.name)

while True:
	CurrentDataPacket=input("write some thing\n\r")
	write1=serialPort1.write(str.encode(CurrentDataPacket))#6
	#write1=serialPort1.write(b"dolly")#
	read1=serialPort1.readlines() #b'dolly
	print(read1)
	
	#write2=serialPort2.write(str.encode(CurrentDataPacket))

	#read2=serialPort2.readlines()
	#print("reading in port_2 : ",read2)
	
'''
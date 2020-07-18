import requests 


location = "Bangalore,in"
payload = {'appid ':"f30e39bd1038401870990a855fe1c089",'q':location}
appid  = "f30e39bd1038401870990a855fe1c089"
url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+appid
print(url)
response = requests.get(url)
print(response.json())


print("\r\n________date time details________\r\n")


import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)
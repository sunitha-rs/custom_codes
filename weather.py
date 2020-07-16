import requests 

location = "Mysore,in"
payload = {'appid ':"f30e39bd1038401870990a855fe1c089",'q':location}
appid  = "f30e39bd1038401870990a855fe1c089"
url = "http://api.openweathermap.org/data/2.5/weather?q="+location+"&APPID="+appid
print(url)
response = requests.get(url)
print(response.json())
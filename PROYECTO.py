from time import sleep
import http.client, urllib
from dhtxx import DHT11, DHT22
from RPLCD import CharLCD
from rpi_TM1638 import TMBoards
# SE DECLARAN LOS PINES A UTILIZAR
dht11 = DHT11(14)
DIO = 16
CLK = 20
STB = 21
lcd = CharLCD(cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])

TM = TMBoards(DIO, CLK, STB, 0)
TM.clearDisplay()

TM.leds[0] = True
TM.leds[2] = True
TM.leds[7] = True

TM.segments[0] = 'HOLA'
TM.segments[4] = 'SAMY'

while True:
    lcd.write_string("Time: %s" %time.strftime("%H:%M:%S"))
    
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Date: %s" %time.strftime("%m/%d/%Y"))

while True:
 # Retries 'max_tries' from DHT11 to get a valid result
 r = dht11.get_result(max_tries=10)  # 'max_tries' defaults to 5
 if r:
  print('Temp: {0:0.1f} C Humidity; {1:0.1f} %'.format(r[0], r[1]))
  params = urllib.parse.urlencode({'field1': r[0],'field2': r[1], 'key':'VZDHT6DSIFYZ5UYT'})
  headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
  conn = http.client.HTTPConnection("api.thingspeak.com:80")
  try:
   conn.request("POST", "/update", params, headers)
   response = conn.getresponse()
   print(response.status, response.reason)
   data = response.read()
   conn.close()
  except:
   print("connection failed")
  sleep(2)
 else:
  print('Failed to get result !')
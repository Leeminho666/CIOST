from gpiozero import LED, Button, Servo, DistanceSensor, Device
from datetime import datetime
from signal import pause
from time import sleep
import MySQLdb
import time
import adafruit_dht
import board
import requests

dht = adafruit_dht.DHT22(board.D2, None)

led = LED(5)
servo = Servo(16)
button1 = Button(3)
button2 = Button(13)
button3 = Button(19)
button4 = Button(26)
button5 = Button(6)

while True:
    while True:
        if button1.is_pressed:
            id = 211301
            break
        elif button2.is_pressed:
            id = 211302
            break
        elif button3.is_pressed:
            id = 211303
            break
        elif button4.is_pressed:
            id = 211304
            break
        elif button5.is_pressed:
            id = 'INVALID'
            break

    while True:
        sleep(0.3)
        now = datetime.now()

        if id == 'invalid' or id == 'INVALID':
            print('\n ID  :', id)
            print("DATE : " + str(now)[:10] + " \nTIME :" + str(now)[10:19])
            print("~~~NO ENTRY~~~")
            break
        else:
            print('\n ID  :', id)
            print("DATE : " + str(now)[:10] + " \nTIME :" + str(now)[10:19])
            temperature = dht.temperature
            humidity = dht.humidity
            if temperature <= 37.5:
                print("Temp : {:.1f} *C".format(temperature) + "\n~~~Please ENTER~~~")
                sleep(1)
                led.on()
                servo.max()    
                sleep(5)
                led.blink(0.2,0.2,None,True)
                sleep(5)
                servo.min()
                led.off()
            else:
                print("Temp\t : {:.1f} *C".format(temperature) + "\n~~~~~No Entry~~~~~")

            temp = str(temperature)
            time = now.strftime("'%H%M%S'")
            date = now.strftime('%Y%m%d')
            id = str(id)
            db = MySQLdb.connect("10.0.126.53", "jovin-test13/12", "123", "jovin-test1")
            cursor = db.cursor()
            sql = "UPDATE try1 SET Temp = " + temp + " WHERE ID = " + id + ""
            cursor.execute(sql)
            db.commit()
            print(cursor.rowcount, "record(s) affected\n")
            response = requests.get("http://10.0.126.53:1880/clockinoutsystm")
            print(response.status_code)
            break

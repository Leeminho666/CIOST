import requests
import datetime
import time
import request
import paho.mqtt.client as mqtt
import time



import mysql.connector
mydb = mysql.connector.connect(
  host="your host",
  user="your sql username",
  password="your sql password",
  database="youe sql database"
)



while True:
  id = input("id\t:")

  mycursor = mydb.cursor()

  idinsql = "SELECT ID FROM try1 WHERE ID = "+id+""
  mycursor.execute(idinsql)
  x = mycursor.fetchone()

  if (x != None):
    temp = input("Temperature\t:")
    tempt = float(temp)
    if (tempt < 37.5):
      print("you may enter")
    else:
      print("high body temperature no entry")
  else:
    print("no such id, no entry")


  now = datetime.datetime.now()
  tiMe = now.strftime("'%H:%M:%S'")
  daTe = now.strftime("%Y%m%d")


  sql = "UPDATE try1 SET Temp = "+temp+" WHERE ID = "+id+""
  print(sql)
  mycursor.execute(sql)

  mydb.commit()


  def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

  client = mqtt.Client()
  client.on_connect = on_connect
  client.connect("localhost", 1883, 60)

# send a message to the raspberry/topic every 1 second, 5 times in a row

  # the four parameters are topic, sending content, QoS and whether retaining the message respectively
  client.publish('test/test1', payload=id + temp, qos=0, retain=False)
  print(f"send {id} to test/test1")


  #client.loop_forever()

'''
  print(mycursor.rowcount, "record(s) affected")
  response = requests.get("http://localhost:1880/clockinoutsystem")
  print(response.status_code)'''
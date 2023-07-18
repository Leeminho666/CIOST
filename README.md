# CIOST
Clock In Out System With Temperature Detector

Demo project of a clock in and out system with temperature sensor.

A raspberry pi is used to get the necessary inputs and storing them in mySQL
the nodeRed program will get the data needed from mySQL and display it in a local site.

Get your node-red running, copy the source code from the file then paste in the import window in node-red

 run the python program


**MQTT node can be change to HTTP if u dont have the tools needed for MQTT like mosquitto
**configure ur own http link join to the nodes and change  
**comment out the mqtt codes lin53-64 and uncomment the HTTP codes line70-72
**the tester node was just used to test things out

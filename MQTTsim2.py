from random import random
from random import randrange
import paho.mqtt.client as mqtt #import the client1
import time

########################################
def on_message(client, userdata, message):
    #mssg =(message.topic ,str(message.payload.decode("utf-8")))
    mssg = str(message.payload.decode("utf-8"))
    global a 
    if message.topic == "Command":
        if not mssg == "run":
            a = 0
            print("Simulatie stop")
        # else:
            # print("Simulatie running")
    # print("message received " ,)
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)
########################################

def on_log(client, userdata, level, buf):
    print("log: ",buf)

print("reading IO list")
chn = list()
f = open("IOlist.txt", "r")
for x in f:
    chn.append(x[:-1]) 
f.close

# broker_address="localhost"
broker_address="192.168.1.13"
# broker2_address="192.168.5.134"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message = on_message #attach function to callback
# client.on_log = on_log #attach function to log callback
# client2 = mqtt.Client("P1") #create new instance
# client2.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
# client2.connect(broker2_address) #connect to broker
# client2.loop_start() #start the loop

print("Subscribing to topic","chris")
client.subscribe("chris")
print("Publishing message to topic","chris")

client.publish("Command","run", 0, True)
for ch in chn:
    client.subscribe(ch)
a = 1
print("start loop")
loopcounter = 0
while a == 1:
    client.subscribe("Command")
    if loopcounter >= 100:
        for ch in chn:
            if ch[:1] =="t" or ch[:3] =="cvt":
                rnd = randrange(10,30)
            elif ch[:3] =="drk":
                rnd = randrange(0,4)
            elif ch[:3] =="pos":
                rnd = randrange(0,100)
            elif ch[:3] =="rpm":
                rnd = randrange(0,100)
            else:
                rnd = randrange(0,2)
            # print(ch)
            # client.publish(ch.channelName,rnd)
            if not(ch[:2] =="hr" or ch[:2] =="vt" or ch[:2] =="rv"or ch[:3] =="rpm" or ch[:3] =="pos"):
                client.publish(ch,rnd, 0, True)
            # client2.publish(chn[ch].Description,rnd, 0, True, "homeassistant")
        loopcounter = 0
        # client.publish("Command","run", 0, True)
    time.sleep(0.05) # wait
    loopcounter = loopcounter + 1
    # print("nog eens")
client.loop_stop() #stop the loop
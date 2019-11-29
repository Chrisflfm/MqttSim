import paho.mqtt.client as mqtt #import the client1
import time
import dm_Channel
from random import random
from random import randrange

########################################
def on_message(client, userdata, message):
    print(message.topic ,str(message.payload.decode("utf-8")))
    # print("message received " ,str(message.payload.decode("utf-8")))
    # print("message topic=",message.topic)
    # print("message qos=",message.qos)
    # print("message retain flag=",message.retain)
########################################

chn = dm_Channel.dm_Channel.getAllChannels()

broker_address="192.168.1.4"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","chris")
client.subscribe("chris")
print("Publishing message to topic","chris")
for ch in chn:
    client.subscribe(chn[ch].Description)

while True
    for ch in chn:
        rnd = randrange(10,30)
        # client.publish(ch.channelName,rnd)
        client.publish(chn[ch].Description,rnd)
    time.sleep(4) # wait
client.loop_stop() #stop the loop
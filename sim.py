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

broker_address="localhost"
# broker_address="192.168.1.13"
# broker2_address="192.168.5.134"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
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
for ch in chn:
    client.subscribe(chn[ch].Description)
a = 1
B = 1
while a == 1:
    for ch in chn:
        if chn[ch].ioLengte > 1:
            rnd = randrange(10,30)
            if B == 0 :
                f = open("MqttSetupsensor.txt", "a")
                # f.write("sensor:\n")
                f.write("  - platform: mqtt\n")
                f.write("    name: \"" + chn[ch].Description +"\"\n")
                f.write("    state_topic: \"" + chn[ch].Description +"\"\n")
                f.write("    unit_of_measurement: 'C'\n")
                f.write("    device_class: \"temperature\"\n\n")
                f.close()
        else:
            rnd = randrange(0,2)
            if B == 0 :
                f = open("MqttSetupbinary_sensor.txt", "a")
                # f.write("binary_sensor:\n")
                f.write("  - platform: mqtt\n")
                f.write("    name: \"" + chn[ch].Description +"\"\n")
                f.write("    state_topic: \"" + chn[ch].Description +"\"\n")
                f.write("    payload_on: \"1\"\n")
                f.write("    payload_off: \"0\"\n")
                f.write("    qos: 0\n\n")
                f.close()
        # client.publish(ch.channelName,rnd)
        client.publish(chn[ch].Description,rnd, 0, True, "homeassistant/sensor/garden/config")
        
        # client2.publish(chn[ch].Description,rnd, 0, True, "homeassistant")
    B = 1
    time.sleep(30) # wait
    print("nog eens")
client.loop_stop() #stop the loop
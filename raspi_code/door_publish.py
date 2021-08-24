#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from ir_sensor import ir_door_state
import time

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt

def on_publish(client,userdata,result):             #create function for callback
    print("data published ", time.time())

def main():
    client = mqtt.Client("lv10_door_pub")  # Create instance of client with client ID “lv10_door”
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_publish = on_publish   
    client.connect('fc94:d59f:f1a3:7abb:6cfb:d58e:382d:349d', 1883)
    client.loop_start()  # Start networking daemon
    while True:
        client.publish("door/lv10_door/door_states",ir_door_state())
        time.sleep(1)

if name == 'main':
    main()
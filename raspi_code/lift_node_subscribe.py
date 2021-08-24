#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from queue import Queue
from bluetooth.ble import GATTRequester
from switchbot import open_door

req = GATTRequester('CF:66:2A:0C:E7:4F',False)
q = Queue()
client = mqtt.Client("lv10_door_sub")

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("door/lv10_door/door_requests")

def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    q.put(msg)

def main():
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_message = on_message  # Define callback function for receipt of a message
    client.connect("fc94:cec3:39f9:6e9e:ec86:a600:ead4:d41a", 1883)
    client.loop_start()  # Start networking daemon
    while True:
        if q.empty() is False:
            state = int(q.get().payload)
            print(state)
            open_door(req, state)

if name == 'main':
    main()
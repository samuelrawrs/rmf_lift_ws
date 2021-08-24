#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt

def on_publish(client,userdata,result):             #create function for callback
    print("data published ", time.time())

def main():
    client = mqtt.Client("lift_pub")  # Create instance of client with client ID “lift”
    client.on_connect = on_connect  # Define callback function for successful connection
    client.on_publish = on_publish   
    client.connect('fc94:cec3:39f9:6e9e:ec86:a600:ead4:d41a', 1883)  # husarnet ipv6 address
    client.loop_start()  # Start networking daemon
    while True:
        #include lift msg
        client.publish("lift/lift_states", ??)
        time.sleep(1)

if name == 'main':
    main()
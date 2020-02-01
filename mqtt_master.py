#!/usr/bin/env python3

from paho.mqtt.client import MQTTv311
import paho.mqtt.client as mqtt
import time

MQTT_ID = "mqtt_master"
MQTT_QUEUE_REQUEST = "/topic/request"
MQTT_QUEUE_RESPONSE = "/topic/response"

 
def on_connect(client, userdata, flags, rc):
	print("Subscribe: {}".format(MQTT_QUEUE_RESPONSE))
	client.subscribe(topic=MQTT_QUEUE_RESPONSE)
 

def on_message(client, userdata, message):
	msg = message.payload.decode("UTF-8")
	print("Payload: {}".format(msg))


def on_publisher(client):
	count = 1
	while True:
		time.sleep(5)
		print("-------------------------")
		print("Sending test message {}...".format(count))
		client.publish(MQTT_QUEUE_REQUEST, "MESSAGE {}".format(count))
		count +=1

 
def main():
	client = mqtt.Client(client_id=MQTT_ID, clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("127.0.0.1", 1883, 60)
	client.loop_start()
	on_publisher(client)

 
if __name__ == "__main__":
	main()


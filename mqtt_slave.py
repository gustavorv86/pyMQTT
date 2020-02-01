#!/usr/bin/env python3

from paho.mqtt.client import MQTTv311
import paho.mqtt.client as mqtt

MQTT_ID = "mqtt_slave_1"
MQTT_QUEUE_REQUEST = "/topic/request"
MQTT_QUEUE_RESPONSE = "/topic/response"


def on_connect(client, userdata, flags, rc):
	print("Subscribe: {}".format(MQTT_QUEUE_REQUEST))
	client.subscribe(MQTT_QUEUE_REQUEST)


def on_message(client, userdata, message):
	print("------------------------------")
	msg = message.payload.decode("UTF-8")
	print("Payload: {}".format(msg))
	client.publish(MQTT_QUEUE_RESPONSE, "RECEIVED {}".format(msg))


def main():
	client = mqtt.Client(client_id=MQTT_ID, clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("127.0.0.1", 1883, 60)
	client.loop_forever()

 
if __name__ == "__main__":
	main()


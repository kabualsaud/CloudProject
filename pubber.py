import paho.mqtt.client as mqtt
# This is the Publisher
client = mqtt.Client()
client.connect("localhost",8882,8080)
client.publish("topic/test", "Hello world!");
client.disconnect();

import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv

load_dotenv()

client_username = os.getenv("MQTT_USERNAME")
client_password = os.getenv("MQTT_PASSWORD")

client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username=client_username, password=client_password)

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"MQTT Connected with result code {reason_code}")

def on_disconnect(client, userdata, flags, reason_code, properties):
    print("MQTT diconnected")

client.on_connect = on_connect
client.on_disconnect = on_disconnect
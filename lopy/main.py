from network import WLAN
from simple import MQTTClient
import machine
import time
import config
import ujson
import pycom


DISCONNECTED = 0
CONNECTING = 1
CONNECTED = 2
state = DISCONNECTED
connection = None
color = 0x00FF00

pycom.heartbeat(False)

wlan = WLAN(mode=WLAN.STA)
wlan.antenna(WLAN.INT_ANT)

def pub_msg(msg):
  global connection

  connection.publish(topic=config.TOPIC, msg=msg, qos=0)
  print('Sending: ' + msg)

def _recv_msg_callback(topic, msg):
  global color

  print("Received: {} from Topic: {}".format(msg, topic))

  try:
    parsed = ujson.loads(msg)
    color = int(parsed['state']['desired']['color'], 0)
    pycom.rgbled(color)
  except ValueError as e:
    print("Exception occured while parsing state")
    return

def run():
  global state, connection, color

  while True:
    while state != CONNECTED:
      try:
        state = CONNECTING
        connection = MQTTClient(client_id=config.CLIENT_ID,
                                server=config.AWS_HOST,
                                port=config.AWS_PORT,
                                keepalive=10000,
                                ssl=True,
                                ssl_params={
                                  "certfile": config.AWS_CLIENT_CERT,
                                  "keyfile": config.AWS_PRIVATE_KEY,
                                  "ca_certs": config.AWS_ROOT_CA
                                })
        connection.connect()
        state = CONNECTED
      except:
        print('Could not establish MQTT connection')
        time.sleep(0.5)
        continue

    print('MQTT LIVE!')
    pycom.rgbled(color)

    # Subscribe for messages
    connection.set_callback(_recv_msg_callback)
    connection.subscribe(config.TOPIC)

    while state == CONNECTED:
      try:
        connection.check_msg()
      except:
        pass
      time.sleep(0.1)

      #msg = '{"device_id":"some_id", "data":"some_data"}'
      #pub_msg(msg)
      #time.sleep(2.0)

nets = wlan.scan()
for net in nets:
  if net.ssid == config.WIFI_SSID:
    print(net.ssid +" was found!")
    wlan.connect(net.ssid, auth=(WLAN.WPA2, config.WIFI_PASS), timeout=5000)
    
    while not wlan.isconnected():
      machine.idle()
    print('Connected to '+ net.ssid)
    run()
    break

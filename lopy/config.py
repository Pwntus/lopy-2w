# WiFi configuration
WIFI_SSID = 'ODS-lab24'
WIFI_PASS = ''

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'a3k7odshaiipe8.iot.eu-west-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/root.pem'
AWS_CLIENT_CERT = '/flash/cert/cert.pem'
AWS_PRIVATE_KEY = '/flash/cert/privkey.pem'

THING_NAME = "00001301"
CLIENT_ID = "00001301"
TOPIC = "$aws/things/00001301/shadow/update"

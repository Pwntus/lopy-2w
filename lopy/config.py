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

################## Subscribe / Publish client #################
#CLIENT_ID = 'PycomPublishClient'
#TOPIC = '$aws/things/00001301/shadow/update'
#OFFLINE_QUEUE_SIZE = -1
#DRAINING_FREQ = 2
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5
#LAST_WILL_TOPIC = '$aws/things/00001301/shadow/update'
#LAST_WILL_MSG = 'To All: Last will message'

####################### Shadow updater ########################
#THING_NAME = "00001301"
#CLIENT_ID = "00001301"
#TOPIC = "$aws/things/00001301/shadow/update"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Delta Listener ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "DeltaListener"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Shadow Echo ########################
#THING_NAME = "00001301"
#CLIENT_ID = "ShadowEcho"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

import time
import ttn
import appconfig


csvfile = open("data.csv", "w")

def uplink_callback(msg, client):
  print("Received uplink from ", msg.dev_id)
  print(msg)
  vbat = msg.payload_fields.Vbat
  cap0 = msg.payload_fields.cap0
  cap1 = msg.payload_fields.cap1
  moi0 = msg.payload_fields.moi0
  moi1 = msg.payload_fields.moi1
  temp0 = msg.payload_fields.temp0
  temp1 = msg.payload_fields.temp1
  rssi = msg.gateways[0].rssi
  snr = msg.gateways[0].snr
  csvfile.write('{},{},{},{},{},{},{},{},{},{}\n'.format(msg.counter, vbat, cap0, cap1, moi0, moi1, temp0, temp1, rssi, snr))


handler = ttn.HandlerClient(appconfig.app_id, appconfig.access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()
time.sleep(600000)
mqtt_client.close()

# using application manager client
app_client =  handler.application()
my_app = app_client.get()
print(my_app)
my_devices = app_client.devices()
print(my_devices)


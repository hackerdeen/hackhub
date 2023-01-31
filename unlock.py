from paho import mqtt
import paho.mqtt.client as paho
from random import randrange
from functools import partial
from time import sleep
from __future__ import print_function
import hackhub

unlock_done = False

def on_msg(msg_id, c, ud, msg):
    global unlock_done
    m = msg.payload.decode("utf-8")
    if f"<{msg_id}>" in m:
        unlock_done = True

def unlock(user=None):
    global unlock_done
    unlock_done = False
    c = paho.Client(client_id="hackhub", userdata=None, protocol=paho.MQTTv5)
    c.username_pw_set(hackhub.MQTT_BROKER_USER, hackhub.MQTT_BROKER_PW)
    msg_id = randrange(int(1e9))

    c.on_message = partial(on_msg, msg_id)
    c.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    c.connect(hackhub.MQTT_BROKER, hackhub.MQTT_BROKER_PORT)
    c.subscribe(f"test")

    c.publish(f"cmd", f"<{msg_id}>OUT1=ON,30")

    c.loop_start()
    times = 0
    while not unlock_done:
        if times > 4000:
            c.loop_stop()
            return False, "Timeout waiting for lock ot ACK command"
        times += 1
        sleep(0.001)
    c.loop_stop()
    return True, "unlocked"

if __name__=="__main__":
    print(unlock())

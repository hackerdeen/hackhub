import hackhub
from paho import mqtt
import paho.mqtt.client as paho
from random import randrange
from functools import partial
from concurrent.futures import Future, TimeoutError

def on_msg(msg_id, fut, c, ud, msg):
    m = msg.payload.decode("utf-8")
    if f"<{msg_id}>" in m:
        fut.set_result(True)
        
def unlock(user=None):
    c = paho.Client(client_id="hackhub", userdata=None, protocol=paho.MQTTv5)
    c.username_pw_set(hackhub.MQTT_BROKER_USER, hackhub.MQTT_BROKER_PW)
    msg_id = randrange(int(1e9))
    fut = Future()
    c.on_message = partial(on_msg, msg_id, fut)
    c.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
    c.connect(hackhub.MQTT_BROKER, hackhub.MQTT_BROKER_PORT)
    c.subscribe(f"{hackhub.LOCK_DEVICE_ID}/ack")
    c.publish(f"{hackhub.LOCK_DEVICE_ID/cmd", f"<{msg_id}>{hackhub.LOCK_UNLOCK_CMD}")
    c.loop_start()
    try:
        res = fut.result(timeout=5)
    except TimeoutError:
        c.loop_stop()
        return False, "Timeout waiting for lock to ACK command"
    c.loop_stop()
    return res, "unlocked"

if __name__=="__main__":
    print(unlock())


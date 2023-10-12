import paho.mqtt.client as mqtt
import numpy as np
import time
import json
import random
import argparse

def demo_get_data(f):
    ts = int(np.round(time.time() * 1000))
    x = np.sin(2 * np.pi * f * ts / 1000)
    return (ts, x)

def init_packet():
    msg = []
    return msg

def add_measurement(msg, f):
    x = demo_get_data(f)
    msg.append({})
    msg[-1]['ts'] = x[0]
    msg[-1]['x'] = x[1]
    return msg

def convert_to_offsets(msg):
    for i in range(len(msg)):
        msg[i]['ts'] = msg[i]['ts'] - msg[-1]['ts']

    return msg

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test data and send to MQTT topic.")

    parser.add_argument('-H', '--host', type=str, default='test.mosquitto.org',
                            help='MQTT Broker Host')
    parser.add_argument('-P', '--port', type=int, default=1883,
                            help='MQTT Broker Port')
    parser.add_argument('-T', '--topic', type=str, default='visualizer/data',
                            help='Topic to publish data to')
    parser.add_argument('-i', '--id', type=str, default='timeless_client_python_' + str(random.randint(1e6, 2e6)),
                            help='Client ID')
    parser.add_argument('-f', '--frequency', type=float, default=1.0/30,
                            help='Dummy Data Oscillation Frequency')
    parser.add_argument('-s', '--samplerate', type=int, default=2,
                            help='Dummy Data Sample Rate')
    parser.add_argument('-p', '--packetsize', type=int, default=4,
                            help='packet size')
    parser.add_argument('--timeless', action='store_true',
                            help='Send timeless packets')

    args = parser.parse_args()

    client = mqtt.Client(args.id)
    client.on_connect = on_connect
    client.connect(args.host, args.port)   
    client.loop_start()

    count = 0
    msg = init_packet()

    while True:
        
        msg = add_measurement(msg, args.frequency)
        count += 1

        if count == args.packetsize:
            # publish messages
            if args.timeless:
                msg = convert_to_offsets(msg)
            
            msg = json.dumps(msg)
            result = client.publish(args.topic, msg)
            if result[0] != 0:
                print(f"Failed to send message to topic {args.topic}")
            else:
                print(f"Sent \"{msg}\" to {args.topic}")

            msg = init_packet()
            count = 0

        time.sleep(1 / args.samplerate)
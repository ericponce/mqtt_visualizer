# MQTT Visualizer
A webapp for visualizing iot data streams sent over MQTT.
In the future it will also act as a time server for MQTT connected devices.
Also provides python scripts for generating faked MQTT datastreams.

## MQTT Data Format

The visualizer expects data in a JSON format. Data is sent to the topic as an array of objects containing a timestamp ('ts') and data value ('x'). If the final element in the array has a timestamp of zero, the previous timestamps are assumed to be offsets from the time of sending, thus allowing for timeless packets to be sent. 

An example timeless packet with four values:
```json
[
    {"ts": -1515, "x": 0.7358134724439376},
    {"ts": -1009, "x": 0.8033166379579392},
    {"ts": -503, "x": 0.861806267284032},
    {"ts": 0, "x": 0.9103661372805817}
]
```

An example timed packet:
```json
[
    {"ts": 1697070763695, "x": 0.26992829429628373}, 
    {"ts": 1697070764201, "x": 0.16656228470604004}, 
    {"ts": 1697070764703, "x": 0.062163511451031696}, 
    {"ts": 1697070765226, "x": -0.04731559598605477}
]
```
## Configuration

The webapp is configured with a json array that specifies the host, port, and listening topic of each datastream.

### Single Source Example

```json
[
    {
        "source": "test.mosquitto.org",
        "port": 8080,
        "topic": "visualizer/data"
    }
]
```

## Test Scripts

First, setup your environment
```bash
cd test
mkdir env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Then, run the rest script (use -h for more options)
```bash
python publish.py
```


## TODO

### Documentation
- Write instructions for using with AWS amplify

### General
- Add comments!
- Use jsLint to check JSON (and also somehow check against schema)
- Provide easy ability to save and load JSON
- Prevent from closing edit window if JSON fails to pass tests
- convert list of topics from array to map
- improve handling of disconnect state
- create connection between two storage types (mqtt clients and graphs)
- implement 'add' button

### MQTT
- When checking for an already exisitng connection to broker, convert hostname to ip address
- support mqtt authentication
- support QOS other than 1
- support labels for multiple data values in a single stream
- add time server support
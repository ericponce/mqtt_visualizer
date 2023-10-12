# MQTT Visualizer
A webapp for visualizing iot data streams sent over MQTT.
In the future it will also act as a time server for MQTT connected devices.
Also provides python scripts for generating faked MQTT datastreams.

![Screenshot](screenshot.png?raw=true)

## Usage
First, sepcfiy the configuration for the webapp by editing the JSON presented when pressing the edit button on the bottom right corner.
Graphs are created using dygraph and allow for zooming by click-dragging across an x- or y-range.
The view may be restored by double clicking the graph.

Importantly, this webapp connects to a MQTT broker over a websocket, which requires explicit support by the broker.

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
- add ability to customize plot (labels, color, min/max)
- Create graph div only when data is recevied
- cleanup 'app' directory

### MQTT
- When checking for an already exisitng connection to broker, convert hostname to ip address
- support mqtt authentication
- support QOS other than 1
- support labels for multiple data values in a single stream
- add time server support (add a checkbox to configuration or include in json)

### Test
- Add support for testing time server
- Add support for sending multiple datastreams from one instance of a script (currently this requires multiple instances of publish.py)
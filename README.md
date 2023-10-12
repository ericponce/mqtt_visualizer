# mqtt_visualizer
A webapp for visualizing iot data streams sent over MQTT.
In the future it will also act as a time server for MQTT connected devices.
Also provides python scripts for generating faked MQTT datastreams.

## Example Configurations

### Single Source
'''json
[
    {
        "source": "test.mosquitto.org",
        "port": 8080,
        "topic": "visualizer/data"
    }
]
'''

## Test Scripts

```bash
cd test
mkdir env
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

```bash
python publish.py
```

## TODO

### Documentation
- Specify MQTT JSON data format
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
- support mqtt authenitcation
- support QOS other than 1
- support labels for multiple data values in a single stream
- add time server support
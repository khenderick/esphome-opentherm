# Tests

This folder contains a limited set of tests consisting of ESPHome configuration files:
* One for each supported sensor type: `binary_sensor.yaml`, `sensor.yaml`, `button.yaml', `switch.yaml`, `number.yaml`
* One that contains every supported sensor: `all.yaml`

It also contains a script `compile_all.sh` that simply runs `esphome compile xxx.yaml` foreach of the yaml files. If that
runs without errors, it should indicate that all sensor type combinations at least compile.

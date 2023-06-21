# What does this implement?

This component provides support for opentherm devices such as:
* [DIYLess](https://diyless.com/)' Master OpenTherm Shield
* [Ihor Melnyk](http://ihormelnyk.com/opentherm_adapter)' OpenTherm adapter

Those are typically connected to an ESP8266 or ESP32

The functional aspect (OpenTherm communications) is heavily based on [ihormelnyk/opentherm_library](https://github.com/ihormelnyk/opentherm_library).

The goal of this component is not to provide a full-blown climate device, but rather expose a
bunch of OpenTherm data and functionality. To make use of this data and functionality is up to the user. 
This could be by - for example - using the exposed enities in ESPHome/HA automations or by using the 
exposed entities in other components (e.g. a combination of [PID Climate](https://esphome.io/components/climate/pid.html)
and a few [Template Outputs](https://esphome.io/components/output/template.html))

As this is my first component, I'm also looking for constructive criticism on how to enhance this
component where needed.

## Note

This component is currently also in an [open PR to esphome](https://github.com/esphome/esphome/pull/3921),
but has currently a low chance of acceptance since it uses a ~32ms delay in `loop()`. This should be
rewritten to work async.

Feel free to help me out and open a PR with improvements.

## Example entry for `config.yaml`:

Note that the connected boiler might not support all sensors. If warnings are reported about unknown messages
it usually means that the related sensor isn't supported. In that case, just remove that sensor from the config.

```yaml
external_components:
  source: github://khenderick/esphome-opentherm
  components: [opentherm]

opentherm:
  read_pin: 21
  write_pin: 22

sensor:
  - platform: opentherm
    ch_min_temperature:
      name: "CH minimum temperature"
    ch_max_temperature:
      name: "CH maximum temperature"
    dhw_min_temperature:
      name: "DHW minimum temperature"
    dhw_max_temperature:
      name: "DHW maximum temperature"
    dhw_flow_rate:
      name: "DHW flow rate"
    pressure:
      name: "pressure"
    modulation:
      name: "modulation"
    dhw_temperature:
      name: "DHW temperature"
    boiler_temperature:
      name: "boiler temperature"
    boiler_2_temperature:
      name: "boiler 2 temperature"
    return_temperature:
      name: "return temperature"

binary_sensor:
  - platform: opentherm
    ch_active:
      name: "CH active"
    ch_2_active:
      name: "CH 2 active"
    dhw_active:
      name: "DHW active"
    flame_active:
      name: "flame active"
    fault:
      name: "fault"
    diagnostic:
      name: "diagnostic"

switch:
  - platform: opentherm
    ch_enabled:
      name: "CH enabled"
    ch_2_enabled:
      name: "CH 2 enabled"
    dhw_enabled:
      name: "DHW enabled"

number:
  - platform: opentherm
    ch_setpoint_temperature:
      name: "CH setpoint temperature"
      min_value: 20.0
      max_value: 45.0
      step: 0.5
      restore_value: true
    ch_2_setpoint_temperature:
      name: "CH 2 setpoint temperature"
      min_value: 20.0
      max_value: 45.0
      step: 0.5
      restore_value: true
    dhw_setpoint_temperature:
      name: "DHW setpoint temperature"
      min_value: 38.0
      max_value: 60.0
      step: 0.5
      restore_value: true
```

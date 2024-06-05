#!/bin/sh
set -e
esphome compile all.yaml
esphome compile binary_sensor.yaml
esphome compile button.yaml
esphome compile number.yaml
esphome compile sensor.yaml
esphome compile switch.yaml

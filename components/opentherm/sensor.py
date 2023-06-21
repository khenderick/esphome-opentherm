import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_PRESSURE,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_EMPTY,
    ICON_GAUGE,
    ICON_THERMOMETER,
    ICON_EMPTY,
    STATE_CLASS_MEASUREMENT,
    UNIT_PERCENT,
    UNIT_CELSIUS,
    UNIT_EMPTY
)
from . import OpenThermComponent, CONF_OPENTHERM_ID

CONF_CH_MIN_TEMPERATURE = "ch_min_temperature"
CONF_CH_MAX_TEMPERATURE = "ch_max_temperature"
CONF_DHW_MIN_TEMPERATURE = "dhw_min_temperature"
CONF_DHW_MAX_TEMPERATURE = "dhw_max_temperature"
CONF_DHW_FLOW_RATE = "dhw_flow_rate"
CONF_MODULATION = "modulation"
CONF_DHW_TEMPERATURE = "dhw_temperature"
CONF_BOILER_TEMPERATURE = "boiler_temperature"
CONF_BOILER_2_TEMPERATURE = "boiler_2_temperature"
CONF_RETURN_TEMPERATURE = "return_temperature"
CONF_OEM_ERROR_CODE = "oem_error_code"
CONF_OEM_DIAGNOSTIC_CODE = "oem_diagnostic_code"

ICON_HOME_THERMOMETER = "mdi:home-thermometer"
ICON_WATER_THERMOMETER = "mdi:water-thermometer"

UNIT_BAR = "bar"
UNIT_LITERS_PER_MIN = "L/min"

TYPES = [
    CONF_CH_MIN_TEMPERATURE,
    CONF_CH_MAX_TEMPERATURE,
    CONF_DHW_MIN_TEMPERATURE,
    CONF_DHW_MAX_TEMPERATURE,
    CONF_DHW_FLOW_RATE,
    CONF_PRESSURE,
    CONF_MODULATION,
    CONF_DHW_TEMPERATURE,
    CONF_BOILER_TEMPERATURE,
    CONF_BOILER_2_TEMPERATURE,
    CONF_RETURN_TEMPERATURE,
    CONF_OEM_ERROR_CODE,
    CONF_OEM_DIAGNOSTIC_CODE
]

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_OPENTHERM_ID): cv.use_id(OpenThermComponent),
            cv.Optional(CONF_CH_MIN_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_HOME_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ),
            cv.Optional(CONF_CH_MAX_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_HOME_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ),
            cv.Optional(CONF_DHW_MIN_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_WATER_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ),
            cv.Optional(CONF_DHW_MAX_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_WATER_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
            ),
            cv.Optional(CONF_DHW_FLOW_RATE): sensor.sensor_schema(
                unit_of_measurement=UNIT_LITERS_PER_MIN,
                icon=ICON_GAUGE,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT
            ),
            cv.Optional(CONF_PRESSURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_BAR,
                icon=ICON_GAUGE,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_PRESSURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_MODULATION): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                icon=ICON_GAUGE,
                accuracy_decimals=1,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_DHW_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BOILER_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BOILER_2_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_RETURN_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_OEM_ERROR_CODE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_EMPTY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
            ),
            cv.Optional(CONF_OEM_DIAGNOSTIC_CODE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_EMPTY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
            ),
        }
    ).extend(cv.COMPONENT_SCHEMA)
)


async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]
        sens = await sensor.new_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_sensor")(sens))


async def to_code(config):
    hub = await cg.get_variable(config[CONF_OPENTHERM_ID])
    for key in TYPES:
        await setup_conf(config, key, hub)

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import button
from esphome.const import (
    DEVICE_CLASS_RESTART,
    DEVICE_CLASS_WATER
)
from components.opentherm import OpenThermComponent, CONF_OPENTHERM_ID, opentherm

CONF_BOILER_LO_RESET = "boiler_lo_reset"
CONF_CH_WATER_FILLING = "ch_water_filling"

ICON_RESET = "mdi:reset"
ICON_WATER_FILLING = "mdi:format-color-fill"


TYPES = [
    CONF_BOILER_LO_RESET,
    CONF_CH_WATER_FILLING,
]

BoilerLOResetButton = opentherm.class_("BoilerLOResetButton", button.Button)
CHWaterFillingButton = opentherm.class_("CHWaterFillingButton", button.Button)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(CONF_OPENTHERM_ID): cv.use_id(OpenThermComponent),
            cv.Optional(CONF_BOILER_LO_RESET): button.button_schema(
                BoilerLOResetButton,
                device_class=DEVICE_CLASS_RESTART,
                icon=ICON_RESET,
            ),
            cv.Optional(CONF_CH_WATER_FILLING): button.button_schema(
                CHWaterFillingButton,
                device_class=DEVICE_CLASS_WATER,
                icon=ICON_WATER_FILLING,
            )
        }
    ).extend(cv.COMPONENT_SCHEMA)
)


async def to_code(config):
    opentherm_component = await cg.get_variable(config[CONF_OPENTHERM_ID])
    if config_boiler_lo_reset := config.get(CONF_BOILER_LO_RESET):
        b = await button.new_button(config_boiler_lo_reset)
        await cg.register_parented(b, config[CONF_OPENTHERM_ID])
        cg.add(opentherm_component.set_boiler_lo_reset_button(b))
    if config_ch_water_filling := config.get(CONF_CH_WATER_FILLING):
        b = await button.new_button(config_ch_water_filling)
        await cg.register_parented(b, config[CONF_OPENTHERM_ID])
        cg.add(opentherm_component.set_ch_water_filling_button(b))

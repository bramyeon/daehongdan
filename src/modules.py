import modi

#modi.update_module_firmware()
bundle = modi.MODI()

# setup modules
network = bundle.networks[0]

# input modules
environment = bundle.envs[0]
button = bundle.buttons[0]
ir_front = bundle.irs[0]
ir_right = bundle.irs[1]
ir_left = bundle.irs[2]

# output modules
motor_fertilizer = bundle.motors[0]
motor_water = bundle.motors[1]
led = bundle.leds[0]
display = bundle.displays[0]


from machine import Pin, ADC
import time

# Green LEDs on GPIO25
green_led = Pin(14, Pin.OUT)

# Internal blue LED on GPIO2
internal_led = Pin(2, Pin.OUT)

# Light sensor on GPIO34
light_sensor = ADC(Pin(34))

# ADC settings
light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

# Light threshold
threshold = 1800

print("Smart Automatic Lighting System Running...")

while True:

    # Read light sensor value
    light_value = light_sensor.read()

    print("Light value:", light_value)

    # Dark condition
    if light_value > threshold:

        # Turn ON LEDs
        green_led.on()
        internal_led.on()

        print("Dark -> LEDs ON")

    # Bright condition
    else:

        # Turn OFF LEDs
        green_led.off()
        internal_led.off()

        print("Bright -> LEDs OFF")

    time.sleep(0.5)
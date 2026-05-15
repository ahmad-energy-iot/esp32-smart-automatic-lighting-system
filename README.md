# ESP32 Smart Automatic Lighting System

## Deutsch

### Projektbeschreibung
Dieses Projekt demonstriert ein intelligentes automatisches Beleuchtungssystem mit ESP32 und einem LDR-Lichtsensor (Photoresistor).

Der ESP32 misst kontinuierlich die Lichtintensität der Umgebung.  
Wenn die Umgebung dunkel wird, schaltet das System automatisch die LEDs ein.  
Bei ausreichendem Licht werden die LEDs automatisch ausgeschaltet.

Das Projekt basiert auf MicroPython und zeigt grundlegende Smart-Home- und IoT-Konzepte.

---

## Verwendete Komponenten

- ESP32 DevKit V1
- LDR Lichtsensor Modul
- LEDs
- Widerstände
- Breadboard
- Jumper Kabel
- MicroPython

---

## Funktionen

- Automatische Lichtsteuerung
- Echtzeit-Lichtmessung
- Smart Home Grundlagen
- Sensor-Automatisierung
- GPIO-Steuerung
- Analoge Sensorwerte mit ESP32
- Interne und externe LEDs

---

## Schaltungsaufbau

### Verbindungen

| Komponente | ESP32 Pin |
|---|---|
| LDR AO | GPIO34 |
| LDR VCC | 3V3 |
| LDR GND | GND |
| Grüne LEDs | GPIO14 |
| Interne LED | GPIO2 |


## MicroPython Code

```python
from machine import Pin, ADC
import time

green_led = Pin(14, Pin.OUT)
internal_led = Pin(2, Pin.OUT)

light_sensor = ADC(Pin(34))

light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

threshold = 1800

print("Smart Automatic Lighting System Running...")

while True:

    light_value = light_sensor.read()

    print("Light value:", light_value)

    if light_value > threshold:

        green_led.on()
        internal_led.on()

        print("Dark -> LEDs ON")

    else:

        green_led.off()
        internal_led.off()

        print("Bright -> LEDs OFF")

    time.sleep(0.5)
```

---

## Autor

### Ahmad Azroun

Renewable Energy Manager  
IoT & AI Specialist  
Smart Energy Systems Developer

---

---

#  English

## Project Description

This project demonstrates a smart automatic lighting system using ESP32 and an LDR light sensor (photoresistor).

The ESP32 continuously monitors the surrounding light intensity.  
When the environment becomes dark, the system automatically turns ON the LEDs.  
When enough light is detected, the LEDs automatically turn OFF.

The project is developed using MicroPython and demonstrates fundamental Smart Home and IoT concepts.

---

## Components Used

- ESP32 DevKit V1
- LDR Light Sensor Module
- LEDs
- Resistors
- Breadboard
- Jumper Wires
- MicroPython

---

## Features

- Automatic light control
- Real-time light monitoring
- Smart Home fundamentals
- Sensor automation
- GPIO control
- Analog sensor reading with ESP32
- Internal and external LEDs

---

## Circuit Connections

| Component | ESP32 Pin |
|---|---|
| LDR AO | GPIO34 |
| LDR VCC | 3V3 |
| LDR GND | GND |
| Green LEDs | GPIO14 |
| Internal LED | GPIO2 |

---


## MicroPython Code

```python
from machine import Pin, ADC
import time

green_led = Pin(14, Pin.OUT)
internal_led = Pin(2, Pin.OUT)

light_sensor = ADC(Pin(34))

light_sensor.atten(ADC.ATTN_11DB)
light_sensor.width(ADC.WIDTH_12BIT)

threshold = 1800

print("Smart Automatic Lighting System Running...")

while True:

    light_value = light_sensor.read()

    print("Light value:", light_value)

    if light_value > threshold:

        green_led.on()
        internal_led.on()

        print("Dark -> LEDs ON")

    else:

        green_led.off()
        internal_led.off()

        print("Bright -> LEDs OFF")

    time.sleep(0.5)
```

---

## Author

### Ahmad Azroun

Renewable Energy Manager  
IoT & AI Specialist  
Smart Energy Systems Developer

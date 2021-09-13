# Pi-Switch
## About
Pi Switch is a project that turns your Raspberry Pi into multi purpouse on/off switch for your : 
* servers
* computers
* and theoreticaly anything you want to
  
  
## Website

https://mateeees.github.io/Pi-Switch/

## How it works?
Using the python script you turn on one of the three LEDs that shine directly to a photoresistor,which lowers its resistance to a minumum,"shorts the circuit" instead of a power switch, and turns on/off your device. 
## Simple python script:

```python
import RPi.GPIO as GPIO
import time
import sys

print("")
print('\x1b[1;35;40m' + 'SERVERS:' + '\x1b[0m')
print('\x1b[2;33;40m' + 'SERVER1 - 1' + '\x1b[0m')
print('\x1b[2;33;40m' + 'SERVER2 - 2' + '\x1b[0m')
print('\x1b[2;33;40m' + 'SERVER3 - 3' + '\x1b[0m')
val = input('\x1b[1;35;40m' + 'SERVER TO TURN ON:   ' + '\x1b[0m')
print("")
print("")

#IFs

if val == 1:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(14,GPIO.OUT)
        print('\x1b[0;30;42m' + 'LED  ON' + '\x1b[0m')
        GPIO.output(14,GPIO.HIGH)
        time.sleep(2)
        print('\x1b[0;30;41m' + 'LED OFF' + '\x1b[0m')
        GPIO.output(14,GPIO.LOW)

elif val == 2:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(16,GPIO.OUT)
        print('\x1b[0;30;42m' + 'LED  ON' + '\x1b[0m')
        GPIO.output(16,GPIO.HIGH)
        time.sleep(2)
        print('\x1b[0;30;41m' + 'LED OFF' + '\x1b[0m')
        GPIO.output(16,GPIO.LOW)

elif val == 3:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        print('\x1b[0;30;42m' + 'LED  ON' + '\x1b[0m')
        GPIO.output(18,GPIO.HIGH)
        time.sleep(2)
        print('\x1b[0;30;41m' + 'LED OFF' + '\x1b[0m')
        GPIO.output(18,GPIO.LOW)

else:
	print('\x1b[1;37;41m' + 'USE ONE OF THE AVIBLE OPTIONS' + '\x1b[0m')
	raw_input('\x1b[2;31;40m' + 'use any key to continue' + '\x1b[0m'
  
```

## Resources
All resources are opensource,so you can make it to! <br/>
All of these resources are specifically designed for my pourpuses,but it's really easy to change that. For the python script you can just use IDE to change that. <br/>
Something like:
```python
if val == 1:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(14,GPIO.OUT)
        print('\x1b[0;30;42m' + 'LED  ON' + '\x1b[0m')
        GPIO.output(14,GPIO.HIGH)
        time.sleep(2)
        print('\x1b[0;30;41m' + 'LED OFF' + '\x1b[0m')
        GPIO.output(14,GPIO.LOW)
```
To:
```python
if val == 1:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(24,GPIO.OUT)
        print('\x1b[0;30;42m' + 'LED  ON' + '\x1b[0m')
        GPIO.output(24,GPIO.HIGH)
        time.sleep(2)
        print('\x1b[0;30;41m' + 'LED OFF' + '\x1b[0m')
        GPIO.output(24,GPIO.LOW)
```


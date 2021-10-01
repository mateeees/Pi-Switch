# Pi-Switch
## About
Pi Switch is a project that turns your Raspberry Pi into multi purpouse on/off switch for your : 
* servers
* computers
* and theoreticaly anything you want to
  
  
## Website

https://mateeees.github.io/Pi-Switch/

## How it works?
You SSH to the Pi Switch and using the python script you turn on one of the three LEDs that shine directly to a photoresistor,which lowers its resistance to a minumum,"shorts the circuit" instead of a power switch, and turns on/off your device. 
## Build tutorial:
Start with assembling three LED assemblies. It is very easy,just put photoresistor and LED into shrink tube. <br/>
Something like:
![Alt text](ass1.jpg?raw=true "Optional Title")](ass1)
and
![Alt text](ass2.jpg?raw=true "Optional Title")](ass2)
and finish with
![Alt text](ass3.jpg?raw=true "Optional Title")](ass3)



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
(Pins have been changed from 14 to 24) <br/> <br/>
And for the PCB you can either use an editor(i use Eagle) to edit the .BRD file and then export it to your gerber files, or you can use the lazy method. You can just use some pinhead jumper wires to connect it to the different pin.

## Parts list:

### Parts you will need
* 3* Photoresistor (i use the LDR5516 ).
* Switch or pinhead jumper
* Female piheaders
       <br/>-Crimping contants KONPC-SPK-PI,you can buy in bulk,they are really cheap,if you mess up.
       <br/>-Plastic shells for crimping contacts KONPC-SPK-10,buy more of them,they are cheap and you are gona ruin a few by sniping it.
       <br/>-Female 2.54mm pinhead row BL240G-V8,0,buy more of them,they are cheap and you are gona ruin a few by sniping it.
* Male piheaders
       <br/>-Female pihead row (for switch and output ) S1G26C,buy more of them,they are cheap and you are gona ruin a few by sniping it.
* 3* 100Ω Resistors
* 3* Good old 5mm white LEDs(3V)
* Connector/pihead - for output you can either use some kind of 6pin connector or just pinheads.
* PCB
       <br/>-You can either use a multi-purpouse PCB or a printed one.(Order one based on my schematics or just download the gerber .ZIP file from my Github page.)
soldering equipment
       <br/>-Soldering iron
       <br/>-Tin(I recommend >1mm),propably lead free
       <br/>-Some good flux or a soldering paste
       <br/>-Wet sponge for cleaning the soldering iron.
       <br/>-Additional soldering eqpiment like: third arm,soldering iron stand,magnifying glass.....
* Some generic cable
* And obviosuly Raspberry Pi,theoreticly you can use any of the(except pico) but i reccomend one with a ethernet port.

### Optional:

* Wire strippers
* clipers
* Breadboard for testing
* Some generic 2.54mm jumper wires
* Shrink tubes (I recomend two diametrs,one for the LED assembly,and smaller one for generic pourpuses.)




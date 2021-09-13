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
(Pins have been changed from 14 to 24) <br/> <br/>
And for the PCB you can either use an editor(i use Eagle) to edit the .BRD file and then export it to your gerber files, or you can use the lazy method. You can just use some pinhead jumper wires to connect it to the different pin.

## Parts list:

div align="" style=" font-size: 18px">
        <p style="font-size: 20px; color: #7D443E">Parts you will need:</p>
        (All links mentioned here leads to czech sites,but by the model number you can find it elsewhere.)


        <li>3* Photoresistor (i use the  <a id="link" href="https://www.gme.cz/fotorezistor-ldr5516">LDR5516</a> ). </li>
        <li>Switch or pinhead jumper</li>
        <li>Female piheaders </li>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Crimping contants <a id="link" href="https://www.gme.cz/konpc-spk-pi-product-38628">KONPC-SPK-PI</a>,you can buy in bulk,they are really cheap,if you mess up. <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Plastic shells for crimping contacts <a id="link" href="https://www.gme.cz/konektor-konpc-spk-10">KONPC-SPK-10</a>,buy more of them,they are cheap and you are gona ruin a few by sniping it.  <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Female 2.54mm pinhead row <a id="link" href="https://www.gme.cz/konektor-114-ds80g">BL240G-V8,0</a>,buy more of them,they are cheap and you are gona ruin a few by sniping it.
        <li>Male piheaders </li>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Female pihead row (for switch and output ) <a id="link" href="https://www.gme.cz/oboustranny-kolik-s1g26-2-54mm">S1G26C</a>,buy more of them,they are cheap and you are gona ruin a few by sniping it.  <br />
        <li>3* 100Ω Resistors</li>
        <li>3* Good old 5mm white LEDs(3V)</li>
        <li>Connector/pihead - for output you can either use some kind of 6pin connector or just pinheads.</li>
        <li>PCB</li>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -You can either use a multi-purpouse PCB or a printed one.(Order one based on my schematics or just download the gerber .ZIP file from my <a id="link" href="https://github.com/mateeees/Pi-Switch">Github page.</a>)
        <li>soldering equipment</li>
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Soldering iron <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Tin(I recommend >1mm) <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Some good flux or a soldering paste <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Wet sponge for cleaning the soldering iron. <br />
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; -Additional soldering eqpiment like: third arm,soldering iron stand,magnifying glass.....
        <li> Some generic cable</li>
        <li>And obviosuly Raspberry Pi,theoreticly you can use any of the(except pico) but i reccomend one with a ethernet port.</li>
    </div>

    <!--optional-->
    <div align="" style=" font-size: 18px">
        <p style="font-size: 20px; color: #7D443E">Optional:</p>
        <li>Wire strippers</li>
        <li>clipers</li>
        <li>Breadboard for testing</li>
        <li>Some generic 2.54mm jumper wires</li>
        <li>Shrink tubes (I recomend two diametrs,one for the LED assembly,and smaller one for generic pourpuses.)</li>
    </div>
    <!--video-->
    <div align="" style=" font-size: 18px">
        <p style="font-size: 20px; color: #7D443E">Build tutorial:</p>
        <a id="link" href="">Video</a>
        -just test for now
    </div>


    <!--tips-->
    <div align="" style=" font-size: 18px">
        <p style="font-size: 20px; color: #7D443E">Additional tips:</p>
        <li>For PCB manufacturing I recomend <a id="link" href="https://jlcpcb.com/">JLC PCB</a>. It may take a while to get to you ,but if you use cheapest delivery option it's really resonable price.</li>
        <li> If you are amateur in this kind of thing(like me) try it on the breadboard. </li>
    </div>






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
	raw_input('\x1b[2;31;40m' + 'use any key to continue' + '\x1b[0m')






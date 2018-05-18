# projectgaming
School scrum training project

Before you can start monitoring your plants and live that high-life you always have dreamt about you have some configuring to do. 

If you don't already have it, go ahead and install the arduino developing tool from https://www.arduino.cc/en/Main/Software as well as python 3.5 from https://www.python.org/downloads/

Download and open up the file projectgaming/src/arduino/flowerpower/flowerpowerwifi.ino using the Arduino IDE. 
Change the wifi settings at line 11 and 12 accordingly to the wifi-ssid and pass that you will be using.
Verify and upload to the arduino-board using the usb-cable.
Open up the serial monitor (icon in the top right corner) to see that it is functioning properly and to get the IP-adress of the arduino.
You can now save the file and close the arduino IDE.
Plug in the usb-cable to a power supply.

On the raspberry:
Change the IP at line 10 in projectgaming/src/raspberry/Webserver/externals/moistcontrol/arduinoconnection.py to the one retrieved from serialmonitor.
Change the email and password at line 16 and 17 in projectgaming/src/raspberry/Webserver/externals/notification/notificationsender.py to a valid email and password. 

Run start_server.bash and you are good to go :)

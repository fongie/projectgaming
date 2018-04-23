import threading, time
from raspberry.Webserver.externals.moistcontrol.arduinoconnection import ArduinoConnection
from raspberry.Webserver.externals.irrigation.tellstickhandler import TellstickHandler

'''
The Plant class symbolizes a Plant in the system. It handles all communication with the external hardware connected with the plant, such as the moist-sensoring Arduino, and the Tellstick Duo for irrigation.

The class is meant to run as a separate Thread. It loops forever until you call set the variable runSignal to False on the thread, then it stops.

'''
class Plant(threading.Thread):

    ''' Constructor for Plant.
    Params:
        plantID (int), an int identifier.
        wateringTime (int), how long pump is turned on each watering'''
    def __init__(self, *args):
        threading.Thread.__init__(self)

        self.lastMoistReading = 0
        self.plantID = args[0]
        if len(args) > 1:
            self.wateringTime = args[1]
        else:
            self.wateringTime = 3

        self.arduinoConnection = ArduinoConnection()
        self.tellstickHandler = TellstickHandler()
        self.runSignal = True

    ''' When started as a thread, loops forever until runSignal is set to False. '''
    def run(self):
        while self.runSignal:
            self.updateMinDryness()
            time.sleep(1) # how often we poll the Arduino for moistness, in seconds
            # time.sleep(60) # production value

    ''' Get the last moist reading from the Arduino connection to this plant '''
    def getMoistness(self):
        return self.lastMoistReading

    def abortWatering(self):
        pass

    ''' Update with a new moist reading from the Arduino '''
    def updateMinDryness(self):
        self.lastMoistReading = self.arduinoConnection.readValue()

    ''' Water the plant by turning on the pump, keeping it on for self.wateringTime seconds, and turning it off. Raises AssertionError if turning on or turning off was unsuccessful. '''
    def waterPlant(self):
        on = self.tellstickHandler.turnOn()
        if not on:
            raise AssertionError('Cannot turn on water pump using TellstickHandler')
        time.sleep(self.wateringTime)
        off = self.tellstickHandler.turnOff()
        if not off:
            raise AssertionError('WARNING Water pump was turned on but not turned off!')
        return

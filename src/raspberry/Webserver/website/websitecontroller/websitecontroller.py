from raspberry.Webserver.externals.externalscontroller.externalscontroller import ExternalsController

class WebsiteController:
    def __init__(self):
        pass

    def getPlants(self):
        #testdata = ["123", "456", "789"]
        #testd = f1.fuktvarde()
        ec = ExternalsController.getInstance()
        #ec = ExternalsController()
        testd = ec.readPlantStatus(1)
        return testd
        #return 'Hej FlowerPower, nu är vi igång!'
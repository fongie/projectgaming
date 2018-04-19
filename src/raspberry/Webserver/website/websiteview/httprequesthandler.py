from flask import Flask, render_template
from raspberry.Webserver.website.websitecontroller.websitecontroller import WebsiteController
#import fuktvarden as f1

app = Flask(__name__)

@app.route('/')
def showWebsite():
    #testdata = ["123", "456", "789"]
    #testd = f1.fuktvarde()
    wc = WebsiteController()
    testd = wc.getPlants()
    return render_template('index.html', testd = '{}'.format(testd))


# EXPORT FLASK_APP=httprequesthandler.py
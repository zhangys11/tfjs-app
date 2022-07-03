import os, sys, json, uuid
from flask import Flask, render_template, request
import uuid

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # limit to 5MB

# routes

@app.route("/")
@app.route("/ImageClassification")
def ImageClassification():
	return render_template("ImageClassification.html")

@app.route("/ObjectDetection")
def ObjectDetection():
	return render_template("ObjectDetection.html")

@app.route("/ImageSegmentation")
def ImageSegmentation():
	return render_template("ImageSegmentation.html")

@app.route("/StyleTransfer")
def StyleTransfer():
	return render_template("StyleTransfer.html")

@app.route("/FundusImageQualifier")
def FundusImageQualifier():
	return render_template("FundusImageQualifier.html")

@app.route("/Leaf")
def Leaf():
	return render_template("Leaf.html")

@app.route("/about")
def About():
	return "Assembled by Dr. Zhang (oo@zju.edu.cn)"

'''
The Flask dev server is not designed to be particularly secure, stable, or efficient. 
By default it runs on localhost (127.0.0.1), change it to app.run(host="0.0.0.0") to run on all your machine's IP addresses.
0.0.0.0 is a special value that you can't use in the browser directly, you'll need to navigate to the actual IP address of the machine on the network. You may also need to adjust your firewall to allow external access to the port.
The Flask quickstart docs explain this in the "Externally Visible Server" section:
    If you run the server you will notice that the server is only accessible from your own computer, not from any other in the network. This is the default because in debugging mode a user of the application can execute arbitrary Python code on your computer.
    If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply by adding --host=0.0.0.0 to the command line.
'''

import webbrowser
from threading import Timer

def open_browser():
    webbrowser.open_new('http://localhost:5007/')
      
if __name__ =='__main__':
    '''
    Pass 'silent' will not open the browser 
    '''

    print(sys.argv)

    if len(sys.argv) < 2 or not sys.argv[1] == 'silent':
        # use netstat -ano|findstr 5007 to check port use
        Timer(2, open_browser).start()

    app.run(host="0.0.0.0", port=5007, debug = False)
    
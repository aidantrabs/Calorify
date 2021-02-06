#Imports
from flask import Flask, render_template

#Iniitalize Flask app
app = Flask(__name__)

#Front page
@app.route('/')
def indexPage():

    return

#Main method
if __name__ == '__main__':
    app.run(debug = True)
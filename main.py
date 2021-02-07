from flask import Flask, render_template, request
import json
from nutritionix import Nutritionix
from keys import keys_index
import http.client
from urllib.parse import urlencode

nix = Nutritionix(app_id=keys_index[0],
                  api_key=keys_index[1])

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():

    if request.method == 'GET':
        return render_template("foods.html")
 
    if request.method == 'POST':
        food = request.form.get("foods")
        results = nix.search(food, results="0:1").json()
        value = results['hits']
        temp = value[0]
        info = nix.item(id = temp['_id']).json()
        
        #print(info)
        return render_template("info.html", info = info)



@app.route("/exercise", methods = ['POST', 'GET'])
def exercise():
  
    if request.method == 'GET':
        return render_template("exercise.html")
      
    if request.method == 'POST':
        conn = http.client.HTTPSConnection("trackapi.nutritionix.com")
        exercise = request.form.get("exercise")
        payload = urlencode({'query': exercise})
        headers = {
            'x-app-id': keys_index[0],
            'x-app-key': keys_index[1],
            'content': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        conn.request("POST", "/v2/natural/exercise", payload, headers)
        res = conn.getresponse()
        data = res.read()
        info = data.decode("utf-8")
        info = json.loads(info)
        temp = info["exercises"]
        temp2 = temp[0]
        calories = temp2['nf_calories']
        inp = temp2['user_input']
        image = temp2['photo']['highres']
        
        # return render
        return render_template("info.html", calories = calories, inp = inp, image = image)

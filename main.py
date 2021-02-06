from flask import Flask, render_template, request
import json
from nutritionix import Nutritionix

nix = Nutritionix(app_id="c1955429",
                  api_key="4e8e629653b6d84fda5ad79b71b805f2")



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
        print(info)
        return render_template("info.html", info = info)


#Main method
if __name__ == '__main__':
    app.run(debug = True)

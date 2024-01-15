import json
import time
import requests

from flask import Flask, request, render_template
from PIL import Image

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        
        body = json.dumps(
          {
            "version": "db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
             "input": { "prompt": q }
          }
        )
        headers = {
          'Authorization': 'Token r8_9cid7ntGfUtiSAlruikwktPqWim2BWJ3u0tz3',
          'Content-Type': 'application/json'
        }
        
        output = requests.post('https://api.replicate.com/v1/predictions',data=body,headers=headers)
        time.sleep(10)
        
        get_url = output.json()['urls']['get']

        get_result = requests.post(get_url,headers=headers).json()['output']
        #image = Image.open(requests.get(get_result[0], stream=True).raw)

        return(render_template("index.html", result=get_result[0]))

    else:
        return(render_template("index.html", result = "Waiting for picture request..."))

if __name__ == "__main__":
    app.run()
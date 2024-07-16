from flask import Flask, render_template
import json
import requests
import random
import platform
import os

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def generator():
    sub_reddit = os.getenv("SUBREDDITS", "Kubernetes,dockermemes,ProgrammerHumor").split(",")  # Get subreddits from env variable
    url = os.getenv("MEME_API_URL", "https://meme-api.com/gimme/") + random.choice(sub_reddit)  # Get URL from env variable
    meme_data = json.loads(requests.get(url).text)
    print(meme_data)
    meme_image = meme_data["preview"][-1]  # get a medium size meme image

    host = platform.uname()  # details about the host
    
    return render_template("index.html", meme_image=meme_image, host_name=host.node, host_type=host.system, host_arch=host.machine)

if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)

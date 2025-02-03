from flask import Flask, request, jsonify
import replicate
import os

app = Flask(__name__)





output = replicate.run(
    "nightmareai/real-esrgan:f121d640bd286e1fdc67f9799164c1d5be36ff74576ee11c803ae5b665dd46aa",
    input={
        "image": "https://replicate.delivery/pbxt/Ing7Fa4YMk6YtcoG1YZnaK3UwbgDB5guRc5M2dEjV6ODNLMl/cat.jpg",
        "scale": 2,
        "face_enhance": False
    }
)
with open("output.png", "wb") as file:
    file.write(output.read())
#=> output.png written to disk
from flask import Flask, request, jsonify
import replicate
import os
import logging
import base64

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)




input = {
        "image": "https://replicate.delivery/pbxt/Ing7Fa4YMk6YtcoG1YZnaK3UwbgDB5guRc5M2dEjV6ODNLMl/cat.jpg",
        "scale": 2,
        "face_enhance": False
    }


#=> output.jpg written to disk



@app.route('/generate', methods=['POST'])
def generate_image():
    # 获取请求中的输入参数
    print('##############')
    input_data = request.json.get("input")
    logging.info(f"Received input: {input_data}")
    if not input_data:
        return jsonify({"error": "缺少 input 参数"}), 400

    try:
        # 调用 Replicate 模型
        output = replicate.run(
            "nightmareai/real-esrgan:f121d640bd286e1fdc67f9799164c1d5be36ff74576ee11c803ae5b665dd46aa",
            input=input_data
        )
        # with open("output.png", "wb") as file:
        #     file.write(output.read())
        
        # Convert the image data to base64 string
        image_data = output.read()
        base64_image = base64.b64encode(image_data).decode('utf-8')
        # 返回生成的图像 URL
        return jsonify({"image_base64": base64_image})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
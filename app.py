from flask import Flask,request,jsonify,render_template
import os
from flask_cors import CORS,cross_origin
from Kidney_Disease_Classifier.utiles.common import decodeImage
from Kidney_Disease_Classifier.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self) -> None:
        self.filename = ""
        self.classifier = PredictionPipeline(self.filename)
        
@app.route("/",methos=['GET'])
@cross_origin
def home():
    return render_template('index.html')


@app.route("/train",methods=['GET','POST'])
@cross_origin
def trainRoute():
    os.system("dvc repro")
    return "<------training Finished------->"


@app.route("/predict",methods =['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image,clApp.filename) #to base64
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='0.0.0.0',port=8080)
    
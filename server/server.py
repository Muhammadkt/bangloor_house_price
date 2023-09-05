# from flask import Flask,request,jsonify,render_template
# import util
# app=Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('app.html')

# @app.route('/get_location_names')
# def get_location_names():
#     print(util.load_saved_artifacts())
#     response=jsonify({
#         'locations':util.load_saved_artifacts()
#     })
#     response.headers.add('Access-Control-Allow-Orgin','*')
#     print(response)
#     return response
# @app.route('/predict_home_price', methods=['POST'])
# def predict_home_price():
#     total_sqft = float(request.form['total_sqgt'])
#     location = request.form['location']
#     bhk = int(request.form['bhk'])
#     bath = int(request.form['bath'])

#     # Ensure that __data_columns is loaded before using it
#     util.load_saved_artifacts()

#     print("predict_home_price()", util.get_estimated_price(location, total_sqft, bhk, bath))
    
#     # Rest of your code...



# if __name__=="__main__":
#     print("Starting Python Flask Server for Home Price Prediction...")
#     #print(util.get_estimated_price('1st block jayanagar',1000,2,2))
#     app.run()
from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
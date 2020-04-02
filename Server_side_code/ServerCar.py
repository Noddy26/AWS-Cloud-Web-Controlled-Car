import socket
from flask import Flask, request, render_template
from Client_Car import ClientCar
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/forward", methods=['GET'])
def forward():
    ClientCar().move_motors("forward")
    return "true"

@app.route("/left", methods=['GET'])
def left():
    ClientCar().move_motors("left")
    return "true"

@app.route("/right", methods=['GET'])
def right():
    ClientCar().move_motors("right")
    return "true"

@app.route("/backward", methods=['GET'])
def backward():
    ClientCar().move_motors("backward")
    return "true"

@app.route("/up", methods=['GET'])
def up():
    ClientCar().move_motors("up")
    return "true"

@app.route("/LEFT", methods=['GET'])
def LEFT():
    ClientCar().move_motors("LEFT")
    return "true"

@app.route("/RIGHT", methods=['GET'])
def RIGHT():
    ClientCar().move_motors("RIGHT")
    return "true"

@app.route("/down", methods=['GET'])
def down():
    ClientCar().move_motors("down")
    return "true"

@app.route("/left_light_on", methods=['GET'])
def left_light_on():
    ClientCar().move_motors("left_light_on")
    return "true"

@app.route("/right_light_on", methods=['GET'])
def right_light_on():
    ClientCar().move_motors("right_light_on")
    return "true"

@app.route("/left_light_off", methods=['GET'])
def left_light_off():
    ClientCar().move_motors("left_light_off")
    return "true"

@app.route("/right_light_off", methods=['GET'])
def right_light_off():
    ClientCar().move_motors("right_light_off")
    return "true"

@app.route('/')
def static_page():
    return render_template('hi.html')

if __name__ == "__main__":
    app.run(debug=True, host="your ip", port=8080)

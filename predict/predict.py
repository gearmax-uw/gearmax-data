from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/car/predict", methods=['GET', 'POST'])
@cross_origin()
def predict_car_price():
    if request.method == 'POST':
        data = request.get_json()
        make = data['make']
        model = data['model']
        body = data['body']
        fuel = data['fuel']
        transmission = data['transmission']
        power = data['power']
        displacement = data['displacement']
        engine = data['engine']
        torquePower = data['torquePower']
        torqueRpm = data['torqueRpm']
        powerRpm = data['powerRpm']
        wheelSystem = data['wheelSystem']
        gear = data['gear']
        year = data['year']
        tank = data['tank']
        cityFuelEconomy = data['cityFuelEconomy']
        highwayFuelEconomy = data['highwayFuelEconomy']
        seat = data['seat']
        color = data['color']
        isNew = data['isNew']

        print('make={}'.format(make))
        return "15000"
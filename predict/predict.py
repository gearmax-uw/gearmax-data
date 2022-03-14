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

        teststr = """
        make = {};
        model = {};
        body = {};
        fuel = {};
        transmission = {};
        power = {};
        displacement = {};
        engine = {};
        torquePower = {};
        torqueRpm = {};
        powerRpm = {};
        wheelSystem = {};
        gear = {};
        year = {};
        tank = {};
        cityFuelEconomy = {};
        highwayFuelEconomy = {};
        seat = {};
        color = {};
        isNew = {};
        """.format(make, model, body, fuel, transmission, 
        power, displacement, engine, torquePower, torqueRpm, 
        powerRpm, wheelSystem, gear, year, tank, cityFuelEconomy, 
        highwayFuelEconomy, seat, color, isNew);

        print(teststr)

        # todo: replace the returned value with the predicted price
        # wrap it from numerical to string
        return "15000"
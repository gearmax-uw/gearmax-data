from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

import pandas as pd
import numpy as np
import pickle
import catboost
# import

myModel = pickle.load(open("../model/pickle", "rb+"))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/car/predict", methods=['GET', 'POST'])
@cross_origin()
def predict_car_price():
    var_dic = {}
    if request.method == 'POST':


        #! mileage = form.cleaned_data.get('mileage')

        data = request.get_json()
        # make = form.cleaned_data.get('make')
        make = data['make']
        # model = request.POST['model']
        model = data['model']
        # body_type = request.POST['body_type']
        body = data['body']
        # fuel_type = request.POST['fuel_type']
        fuel = data['fuel']
        # transmission = request.POST['transmission']
        # transmission_display = request.POST['transmission_display']
        transmission = data['transmission']
        # horsepower = request.POST['horsepower']
        power = data['power']
        # engine_displacement = request.POST['displacement']
        displacement = data['displacement']
        # engine_type = request.POST['engine_type']
        engine = data['engine']
        # torque_power = request.POST['torque_power']
        torquePower = data['torquePower']
        # torque_rpm = request.POST['torque_rpm']
        torqueRpm = data['torqueRpm']
        # power_rpm = request.POST['power_rpm']
        powerRpm = data['powerRpm']
        # wheel_system = request.POST['wheel_system']
        wheelSystem = data['wheelSystem']
        gear = data['gear']
        # year = request.POST['year']
        year = data['year']
        # fuel_tank_volume = request.POST['fuel_tank_volume']
        tank = data['tank']
        # city_fuel_economy = request.POST['city_fuel_economy']
        cityFuelEconomy = data['cityFuelEconomy']
        # highway_fuel_economy = request.POST['highway_fuel_economy']
        highwayFuelEconomy = data['highwayFuelEconomy']
        # maximum_seating = request.POST['maximum_seating']
        seat = data['seat']
        # exterior_color = form.cleaned_data.get('exterior_color')
        color = data['color']
        # is_new = form.cleaned_data.get('is_new')
        isNew = data['isNew']

        var_dic[make] = 1
        var_dic["model_" + model] = 1
        var_dic['is_new'] = isNew
        var_dic[body] = 1
        var_dic[fuel] = 1
        var_dic[color] = 1
        var_dic[transmission] = 1
        var_dic[wheelSystem] = 1
        var_dic[engine] = 1
        var_dic["power_rpm"] = powerRpm
        var_dic["torque_rpm"] = torqueRpm
        var_dic["torque_power"] = torquePower
        var_dic["horsepower"] = power
        var_dic["engine_displacement"] = displacement
        var_dic["mileage"] = 10000
        var_dic["transmission_display"] = transmission
        var_dic["year"] = year
        var_dic["fuel_tank_volume"] = tank
        var_dic["city_fuel_economy"] = cityFuelEconomy
        var_dic["highway_fuel_economy"] = highwayFuelEconomy
        var_dic["maximum_seating"] = seat

        # teststr = """
        # make = {};
        # model = {};
        # body = {};
        # fuel = {};
        # transmission = {};
        # power = {};
        # displacement = {};
        # engine = {};
        # torquePower = {};
        # torqueRpm = {};
        # powerRpm = {};
        # wheelSystem = {};
        # gear = {};
        # year = {};
        # tank = {};
        # cityFuelEconomy = {};
        # highwayFuelEconomy = {};
        # seat = {};
        # color = {};
        # isNew = {};
        # """.format(make, model, body, fuel, transmission,
        # power, displacement, engine, torquePower, torqueRpm,
        # powerRpm, wheelSystem, gear, year, tank, cityFuelEconomy,
        # highwayFuelEconomy, seat, color, isNew)
       
        # myList = [make, model, body, fuel, transmission, power, displacement, engine, torquePower, torqueRpm, powerRpm, wheelSystem, transmission, year, tank, cityFuelEconomy, highwayFuelEconomy, seat]


        car_specs = pd.DataFrame(var_dic, index=[0]).to_numpy().reshape(1,-1)

        price = myModel.predict(car_specs)

        print(str(price))

        # todo: replace the returned value with the predicted price
        # wrap it from numerical to string
        return "15000"
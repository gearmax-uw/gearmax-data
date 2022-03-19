from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

import pandas as pd
import numpy as np
import pickle
import catboost

myModel = pickle.load(open("../model/pickle", "rb+"))

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/car/predict", methods=['GET', 'POST'])
@cross_origin()
def predict_car_price():
    if request.method == 'POST':
        data = request.get_json()

        mileage = data['mileage']
        make = data['make']
        model = data['model']
        body = data['body']
        fuel = data['fuel']
        transmission = data['transmission']
        gear = data['gear']
        power = data['power']
        displacement = data['displacement']
        engine = data['engine']
        torquePower = data['torquePower']
        torqueRpm = data['torqueRpm']
        powerRpm = data['powerRpm']
        wheelSystem = data['wheelSystem']
        year = data['year']
        tank = data['tank']
        cityFuelEconomy = data['cityFuelEconomy']
        highwayFuelEconomy = data['highwayFuelEconomy']
        seat = data['seat']
        color = data['color']
        isNew = data['isNew']

        col_names = ['city_fuel_economy', 'engine_displacement', 'fuel_tank_volume', 'highway_fuel_economy', 'horsepower', 'is_new', 'maximum_seating', 'mileage', 'transmission_display', 'year', 'torque_power', 'torque_rpm', 'power_rpm', 'Convertible', 'Coupe', 'Hatchback', 'Minivan', 'Pickup Truck', 'SUV / Crossover', 'Sedan', 'Van', 'Wagon', 'Boxer 4 cylinder', 'Boxer 6 cylinder', 'Inline 3 cylinder', 'Inline 4 cylinder', 'Inline 5 cylinder', 'Inline 6 cylinder', 'Rotary Engine', 'V10', 'V12', 'V6', 'V8', 'W12', 'W16', 'W8', 'Biodiesel', 'Compressed Natural Gas', 'Diesel', 'Flex Fuel Vehicle', 'Gasoline', 'Hybrid', 'Propane', 'Black', 'Blue', 'Brown', 'Gold', 'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'Silver', 'Teal', 'Unknown', 'White', 'Yellow', 'Automatic Transmission (A)', 'Continuously Variable Transmission (CVT)', 'Dual Clutch Transmission (DCT)', 'Manual Transmission (M)', 'All Wheel Drive (AWD)', 'Four Wheel Drive (4WD)', 'Front Wheel Drive (FWD)', 'Rear Wheel Drive (RWD)', 'Two Wheel Drive (4X2)', 'Acura', 'Alfa Romeo', 'Aston Martin', 'Audi', 'BMW', 'Bentley', 'Bugatti', 'Buick', 'Cadillac', 'Chevrolet', 'Chrysler', 'Daewoo', 'Dodge', 'Eagle', 'FIAT', 'Ferrari', 'Ford', 'GMC', 'Genesis', 'Geo', 'Honda', 'Hummer', 'Hyundai', 'INFINITI', 'Isuzu', 'Jaguar', 'Jeep', 'Kia', 'Lamborghini', 'Land Rover', 'Lexus', 'Lincoln', 'Lotus', 'MINI', 'Maserati', 'Maybach', 'Mazda', 'McLaren', 'Mercedes-Benz', 'Mercury', 'Mitsubishi', 'Nissan', 'Oldsmobile', 'Plymouth', 'Pontiac', 'Porsche', 'RAM', 'Rolls-Royce', 'SRT', 'Saab', 'Saturn', 'Scion', 'Smart', 'Subaru', 'Suzuki', 'Toyota', 'Volkswagen', 'Volvo', 'model_1 Series', 'model_124 Spider', 'model_1500', 'model_1M', 'model_2 Series', 'model_200', 'model_240', 'model_240SX', 'model_3 Series', 'model_3 Series Gran Turismo', 'model_300', 'model_300-Class', 'model_3000GT', 'model_300M', 'model_300ZX', 'model_350-Class', 'model_350Z', 'model_360', 'model_360 Spider', 'model_370Z', 'model_4 Series', 'model_400-Class', 'model_420-Class', 'model_430 Scuderia', 'model_456M', 'model_458 Italia', 'model_488', 'model_4C', 'model_4Runner', 'model_5 Series', 'model_5 Series Gran Turismo', 'model_500', 'model_500-Class', 'model_500L', 'model_500X', 'model_550', 'model_560-Class', 'model_57', 'model_570GT', 'model_570S', 'model_575M', 'model_599 GTB Fiorano', 'model_6 Series', 'model_6 Series Gran Turismo', 'model_600LT', 'model_612 Scaglietti', 'model_626', 'model_650S', 'model_675LT', 'model_7 Series', 'model_718 Boxster', 'model_718 Cayman', 'model_720S', 'model_740', 'model_8 Series', 'model_812 Superfast', 'model_850', 'model_86', 'model_9-2X', 'model_9-3', 'model_9-3 SportCombi', 'model_9-4X', 'model_9-5', 'model_9-5 SportCombi', 'model_9-7X', 'model_900', 'model_911', 'model_918 Spyder', 'model_928', 'model_940', 'model_944', 'model_960', 'model_968', 'model_A-Class', 'model_A3', 'model_A4', 'model_A4 Allroad', 'model_A4 Avant', 'model_A5', 'model_A5 Sportback', 'model_A6', 'model_A6 Allroad', 'model_A7', 'model_A8', 'model_AMG GT', 'model_ATS', 'model_ATS Coupe', 'model_ATS-V', 'model_ATS-V Coupe', 'model_Acadia', 'model_Accent', 'model_Accord', 'model_Accord Coupe', 'model_Accord Crosstour', 'model_Accord Hybrid', 'model_Achieva', 'model_ActiveHybrid 3', 'model_ActiveHybrid 5', 'model_ActiveHybrid 7', 'model_Aerio', 'model_Aerostar', 'model_Alero', 'model_Allante', 'model_Allroad', 'model_Altima', 'model_Altima Coupe', 'model_Amanti', 'model_Amigo', 'model_Armada', 'model_Arnage', 'model_Arteon', 'model_Ascender', 'model_Ascent', 'model_Aspen', 'model_Astra', 'model_Astro', 'model_Astro Cargo', 'model_Atlas', 'model_Atlas Cross Sport', 'model_Aura', 'model_Aurora', 'model_Avalanche', 'model_Avalon', 'model_Avenger', 'model_Aventador', 'model_Aveo', 'model_Aviator', 'model_Axiom', 'model_Azera', 'model_Aztek', 'model_Azure', 'model_B-Series', 'model_B9 Tribeca', 'model_BRZ', 'model_Baja', 'model_Beetle', 'model_Bentayga', 'model_Bentayga Hybrid', 'model_Blackwood', 'model_Blazer', 'model_Bonneville', 'model_Borrego', 'model_Boxster', 'model_Bravada', 'model_Brooklands', 'model_C-Class', 'model_C-HR', 'model_C/K 1500', 'model_C/V', 'model_C30', 'model_C70', 'model_CC', 'model_CL', 'model_CL-Class', 'model_CLA-Class', 'model_CLK-Class', 'model_CLS-Class', 'model_CR-V', 'model_CR-Z', 'model_CT4', 'model_CT5', 'model_CT6', 'model_CTS', 'model_CTS Coupe', 'model_CTS Sport Wagon', 'model_CTS-V', 'model_CTS-V Coupe', 'model_CTS-V Wagon', 'model_CX-3', 'model_CX-30', 'model_CX-5', 'model_CX-7', 'model_CX-9', 'model_Cabrio', 'model_Cabriolet', 'model_Cadenza', 'model_Caliber', 'model_California', 'model_California T', 'model_Camaro', 'model_Camry', 'model_Camry Solara', 'model_Canyon', 'model_Capri', 'model_Caprice', 'model_Captiva Sport', 'model_Caravan', 'model_Carrera GT', 'model_Catera', 'model_Cavalier', 'model_Cayenne', 'model_Cayenne E-Hybrid', 'model_Cayenne Hybrid', 'model_Cayman', 'model_Celica', 'model_Century', 'model_Challenger', 'model_Charger', 'model_Cherokee', 'model_Chevy Van', 'model_Cirrus', 'model_City Express', 'model_Civic', 'model_Civic Coupe', 'model_Civic Hatchback', 'model_Civic Hybrid', 'model_Civic Type R', 'model_Civic del Sol', 'model_Classic', 'model_Cobalt', 'model_Colorado', 'model_Colt', 'model_Commander', 'model_Compass', 'model_Concorde', 'model_Continental', 'model_Continental Flying Spur', 'model_Continental GT', 'model_Continental GTC', 'model_Continental R', 'model_Continental Supersports', 'model_Contour', 'model_Cooper', 'model_Cooper Clubman', 'model_Cooper Coupe', 'model_Cooper Paceman', 'model_Corniche', 'model_Corolla', 'model_Corolla Hatchback', 'model_Corolla iM', 'model_Corsair', 'model_Corsica', 'model_Corvette', 'model_Cougar', 'model_Countryman', 'model_Coupe', 'model_Crossfire', 'model_Crossfire SRT-6', 'model_Crosstour', 'model_Crosstrek', 'model_Crosstrek Hybrid', 'model_Crown Victoria', 'model_Cruze', 'model_Cruze Limited', 'model_Cube', 'model_Cullinan', 'model_Cutlass', 'model_Cutlass Ciera', 'model_Cutlass Supreme', 'model_DB11', 'model_DB7', 'model_DB9', 'model_DBS', 'model_DTS', 'model_Dakota', 'model_Dart', 'model_Dawn', 'model_DeVille', 'model_Defender', 'model_Diablo', 'model_Diamante', 'model_Discovery', 'model_Discovery Series II', 'model_Discovery Sport', 'model_Durango', 'model_E-Class', 'model_E-PACE', 'model_E-Series', 'model_ECHO', 'model_ES', 'model_ES 300', 'model_ES 330', 'model_ES 350', 'model_EX35', 'model_EX37', 'model_Eclipse', 'model_Eclipse Spyder', 'model_EcoSport', 'model_Edge', 'model_Eighty-Eight', 'model_Eighty-Eight Royale', 'model_Elantra', 'model_Elantra Coupe', 'model_Elantra GT', 'model_Elantra Touring', 'model_Eldorado', 'model_Electra', 'model_Element', 'model_Elise', 'model_Enclave', 'model_Encore', 'model_Encore GX', 'model_Endeavor', 'model_Entourage', 'model_Envision', 'model_Envoy', 'model_Envoy XL', 'model_Envoy XUV', 'model_Enzo', 'model_Eos', 'model_Equator', 'model_Equinox', 'model_Equus', 'model_Escalade', 'model_Escalade ESV', 'model_Escalade EXT', 'model_Escape', 'model_Escape Hybrid', 'model_Escort', 'model_Esprit', 'model_Esteem', 'model_EuroVan', 'model_Evora', 'model_Exige', 'model_Expedition', 'model_Explorer', 'model_Explorer Hybrid', 'model_Explorer Sport', 'model_Explorer Sport Trac', 'model_Express', 'model_Express Cargo', 'model_F-150', 'model_F-150 Heritage', 'model_F-150 SVT Lightning', 'model_F-PACE', 'model_F-TYPE', 'model_F12 Berlinetta', 'model_F430', 'model_F430 Spider', 'model_F8 Tributo', 'model_FF', 'model_FJ Cruiser', 'model_FR-S', 'model_FX35', 'model_FX37', 'model_FX45', 'model_FX50', 'model_Fiero', 'model_Fiesta', 'model_Firebird', 'model_Fit', 'model_Five Hundred', 'model_Fleetwood', 'model_Flex', 'model_Flying Spur', 'model_Focus', 'model_Focus RS', 'model_Focus SVT', 'model_Forenza', 'model_Forester', 'model_Forte', 'model_Forte Koup', 'model_Forte5', 'model_Fortwo', 'model_Freelander', 'model_Freestar', 'model_Freestyle', 'model_Frontier', 'model_Fusion', 'model_G-Class', 'model_G25', 'model_G3', 'model_G35', 'model_G37', 'model_G5', 'model_G6', 'model_G70', 'model_G8', 'model_G80', 'model_G90', 'model_GL-Class', 'model_GLA-Class', 'model_GLB-Class', 'model_GLC-Class', 'model_GLE-Class', 'model_GLK-Class', 'model_GLS-Class', 'model_GS', 'model_GS 200t', 'model_GS 300', 'model_GS 350', 'model_GS 400', 'model_GS 430', 'model_GS 460', 'model_GS F', 'model_GS Hybrid', 'model_GT', 'model_GT-R', 'model_GTC4Lusso', 'model_GTC4Lusso T', 'model_GTI', 'model_GTO', 'model_GX', 'model_GX 470', 'model_Galant', 'model_Gallardo', 'model_Genesis', 'model_Genesis Coupe', 'model_Ghibli', 'model_Ghost', 'model_Giulia', 'model_Gladiator', 'model_Golf', 'model_Golf Alltrack', 'model_Golf R', 'model_Golf SportWagen', 'model_GranSport', 'model_GranTurismo', 'model_Grand Am', 'model_Grand Caravan', 'model_Grand Cherokee', 'model_Grand Marquis', 'model_Grand Prix', 'model_Grand Vitara', 'model_Grand Voyager', 'model_Grand Wagoneer', 'model_H3', 'model_H3T', 'model_HHR', 'model_HR-V', 'model_Highlander', 'model_Hombre', 'model_Huracan', 'model_I30', 'model_I35', 'model_ILX', 'model_ILX Hybrid', 'model_ION', 'model_ION Red Line', 'model_IPL G', 'model_IS', 'model_IS 250', 'model_IS 350', 'model_Impala', 'model_Impala Limited', 'model_Imperial', 'model_Impreza', 'model_Impreza WRX', 'model_Impreza WRX STI', 'model_Insight', 'model_Integra', 'model_Intrepid', 'model_Intrigue', 'model_J30', 'model_JX35', 'model_Jetta', 'model_Jetta GLI', 'model_Jetta Hybrid', 'model_Jetta SportWagen', 'model_Jimmy', 'model_Journey', 'model_Juke', 'model_K5', 'model_K900', 'model_Kicks', 'model_Kizashi', 'model_Kona', 'model_L-Series', 'model_L300', 'model_LC', 'model_LFA', 'model_LHS', 'model_LR2', 'model_LR3', 'model_LR4', 'model_LS', 'model_LS 400', 'model_LS 430', 'model_LS 460', 'model_LS 500', 'model_LTD Crown Victoria', 'model_LX', 'model_LX 450', 'model_LX 470', 'model_LX 570', 'model_LaCrosse', 'model_Lancer', 'model_Lancer Evolution', 'model_Lancer Sportback', 'model_Land Cruiser', 'model_Lanos', 'model_Le Baron', 'model_LeSabre', 'model_Legacy', 'model_Leganza', 'model_Levante', 'model_Liberty', 'model_Lucerne', 'model_Lumina', 'model_Lumina Minivan', 'model_M-Class', 'model_M2', 'model_M3', 'model_M30', 'model_M35', 'model_M35h', 'model_M37', 'model_M4', 'model_M45', 'model_M5', 'model_M56', 'model_M6', 'model_M8', 'model_MAZDA2', 'model_MAZDA3', 'model_MAZDA5', 'model_MAZDA6', 'model_MAZDASPEED MX-5 Miata', 'model_MAZDASPEED3', 'model_MAZDASPEED6', 'model_MDX', 'model_MKC', 'model_MKS', 'model_MKT', 'model_MKX', 'model_MKZ', 'model_MP4-12C', 'model_MPV', 'model_MR2', 'model_MR2 Spyder', 'model_MX-5 Miata', 'model_Macan', 'model_Magnum', 'model_Malibu', 'model_Malibu Maxx', 'model_Marauder', 'model_Mariner', 'model_Mariner Hybrid', 'model_Mark LT', 'model_Mark VII', 'model_Mark VIII', 'model_Matrix', 'model_Maxima', 'model_Metris', 'model_Metris Cargo', 'model_Metro', 'model_Milan', 'model_Millenia', 'model_Mirage', 'model_Mirage G4', 'model_Montana', 'model_Montana SV6', 'model_Monte Carlo', 'model_Montego', 'model_Monterey', 'model_Montero', 'model_Montero Sport', 'model_Mountaineer', 'model_Mulsanne', 'model_Murano', 'model_Murano CrossCabriolet', 'model_Murcielago', 'model_Mustang', 'model_Mustang SVT Cobra', 'model_Mustang Shelby GT350', 'model_Mustang Shelby GT500', 'model_NSX', 'model_NV200', 'model_NX', 'model_NX 200t', 'model_Nautilus', 'model_Navigator', 'model_Neon', 'model_Neon SRT-4', 'model_New Yorker', 'model_Ninety-Eight', 'model_Nitro', 'model_Odyssey', 'model_Optima', 'model_Optima Hybrid', 'model_Outback', 'model_Outlander', 'model_Outlander Sport', 'model_Outlook', 'model_P1', 'model_PT Cruiser', 'model_Pacifica', 'model_Palisade', 'model_Panamera', 'model_Panamera E-Hybrid', 'model_Panamera Hybrid', 'model_Park Avenue', 'model_Park Ward', 'model_Paseo', 'model_Passat', 'model_Passport', 'model_Pathfinder', 'model_Patriot', 'model_Phaeton', 'model_Phantom', 'model_Phantom Coupe', 'model_Phantom Drophead Coupe', 'model_Pickup', 'model_Pilot', 'model_Portofino', 'model_Prelude', 'model_Prizm', 'model_ProMaster', 'model_ProMaster City', 'model_Protege', 'model_Protege5', 'model_Prowler', 'model_Q3', 'model_Q40', 'model_Q45', 'model_Q5', 'model_Q50', 'model_Q50 Hybrid', 'model_Q60', 'model_Q7', 'model_Q70', 'model_Q70 Hybrid', 'model_Q70L', 'model_Q8', 'model_QX30', 'model_QX4', 'model_QX50', 'model_QX56', 'model_QX60', 'model_QX70', 'model_QX80', 'model_Quattroporte', 'model_Quest', 'model_R-Class', 'model_R32', 'model_R8', 'model_RAM 1500', 'model_RAM 50 Pickup', 'model_RAM Van', 'model_RAM Wagon', 'model_RAV4', 'model_RC', 'model_RC 200t', 'model_RC 300', 'model_RC 350', 'model_RC F', 'model_RDX', 'model_RL', 'model_RLX Hybrid Sport', 'model_RS 3', 'model_RS 4', 'model_RS 5', 'model_RS 5 Sportback', 'model_RS 6', 'model_RS 7', 'model_RSX', 'model_RX', 'model_RX 300', 'model_RX 330', 'model_RX 350', 'model_RX-8', 'model_Rabbit', 'model_Raider', 'model_Rainier', 'model_Range Rover', 'model_Range Rover Evoque', 'model_Range Rover Hybrid', 'model_Range Rover Hybrid Plug-in', 'model_Range Rover Sport', 'model_Range Rover Velar', 'model_Ranger', 'model_Rapide', 'model_Reatta', 'model_Regal', 'model_Regal Sportback', 'model_Regal TourX', 'model_Regency', 'model_Relay', 'model_Rendezvous', 'model_Renegade', 'model_Reno', 'model_Ridgeline', 'model_Rio', 'model_Rio5', 'model_Riviera', 'model_Roadmaster', 'model_Roadster', 'model_Rodeo', 'model_Rodeo Sport', 'model_Rogue', 'model_Rogue Select', 'model_Rogue Sport', 'model_Rondo', 'model_Routan', 'model_S-10', 'model_S-Class', 'model_S-Class Coupe', 'model_S-Series', 'model_S-TYPE', 'model_S-TYPE R', 'model_S2000', 'model_S3', 'model_S4', 'model_S4 Avant', 'model_S40', 'model_S5', 'model_S5 Sportback', 'model_S6', 'model_S60', 'model_S60 R', 'model_S7', 'model_S70', 'model_S8', 'model_S80', 'model_S90', 'model_SC 400', 'model_SC 430', 'model_SL-Class', 'model_SLC-Class', 'model_SLK-Class', 'model_SLR McLaren', 'model_SLS-Class', 'model_SLX', 'model_SQ5', 'model_SRX', 'model_SS', 'model_SSR', 'model_STS', 'model_STS-V', 'model_SVX', 'model_SX4', 'model_Sable', 'model_Safari', 'model_Safari Cargo', 'model_Santa Fe', 'model_Santa Fe Sport', 'model_Santa Fe XL', 'model_Savana', 'model_Savana Cargo', 'model_Sebring', 'model_Sedona', 'model_Seltos', 'model_Sentra', 'model_Sephia', 'model_Sequoia', 'model_Seville', 'model_Sienna', 'model_Sierra 1500', 'model_Sierra 1500 Limited', 'model_Sierra 1500HD', 'model_Sierra 2500HD', 'model_Sierra Classic 1500', 'model_Silhouette', 'model_Silverado 1500', 'model_Silverado 1500HD', 'model_Silverado 2500', 'model_Silverado 2500HD', 'model_Silverado Classic 1500', 'model_Silverado Classic 1500HD', 'model_Silverado SS', 'model_Sky', 'model_Skylark', 'model_Solstice', 'model_Sonata', 'model_Sonata Hybrid', 'model_Sonic', 'model_Sonoma', 'model_Sorento', 'model_Soul', 'model_Spark', 'model_Spectra', 'model_Sportage', 'model_Spyder', 'model_Stealth', 'model_Stelvio', 'model_Stinger', 'model_Storm', 'model_Stratus', 'model_Suburban', 'model_Sunfire', 'model_Superamerica', 'model_Supra', 'model_T100', 'model_TC', 'model_TL', 'model_TLX', 'model_TSX', 'model_TT', 'model_TT RS', 'model_TTS', 'model_Tacoma', 'model_Tahoe', 'model_Talon', 'model_Taurus', 'model_Taurus X', 'model_Telluride', 'model_Terrain', 'model_Terraza', 'model_Thunderbird', 'model_Tiburon', 'model_Tiguan', 'model_Titan', 'model_Toronado', 'model_Torrent', 'model_Touareg', 'model_Touareg 2', 'model_Touareg Hybrid', 'model_Town & Country', 'model_Town Car', 'model_Tracer', 'model_Tracker', 'model_Trailblazer', 'model_Trailblazer EXT', 'model_Trans Sport', 'model_Transit Cargo', 'model_Transit Connect', 'model_Transit Crew', 'model_Transit Passenger', 'model_Traverse', 'model_Trax', 'model_Tribeca', 'model_Tribute', 'model_Trooper', 'model_Truck', 'model_Tucson', 'model_Tundra', 'model_UX', 'model_Uplander', 'model_Urus', 'model_V12 Vanquish', 'model_V12 Vantage', 'model_V40', 'model_V50', 'model_V60', 'model_V70', 'model_V70 R', 'model_V8', 'model_V8 Vantage', 'model_V90', 'model_VUE', 'model_Vanquish', 'model_Vantage', 'model_Veloster', 'model_Veloster N', 'model_Veloster Turbo', 'model_Venture', 'model_Venue', 'model_Venza', 'model_Veracruz', 'model_Verano', 'model_Verona', 'model_Versa', 'model_Versa Note', 'model_Veyron', 'model_Vibe', 'model_Villager', 'model_Viper', 'model_Virage', 'model_Vitara', 'model_Voyager', 'model_WRX', 'model_WRX STI', 'model_Windstar', 'model_Windstar Cargo', 'model_Wraith', 'model_Wrangler', 'model_Wrangler Unlimited', 'model_X-TYPE', 'model_X1', 'model_X2', 'model_X3', 'model_X3 M', 'model_X4', 'model_X4 M', 'model_X5', 'model_X5 M', 'model_X6', 'model_X6 M', 'model_X7', 'model_XC', 'model_XC40', 'model_XC60', 'model_XC70', 'model_XC90', 'model_XE', 'model_XF', 'model_XF Sportbrake', 'model_XG350', 'model_XJ-Series', 'model_XK-Series', 'model_XL-7', 'model_XLR', 'model_XLR-V', 'model_XT4', 'model_XT5', 'model_XT6', 'model_XTS', 'model_XV Crosstrek Hybrid', 'model_Xterra', 'model_Yaris', 'model_Yaris iA', 'model_Yukon', 'model_Yukon XL', 'model_Z3', 'model_Z3 M', 'model_Z4', 'model_Z4 M', 'model_Z8', 'model_ZDX', 'model_Zephyr', 'model_i-Series', 'model_iA', 'model_iM', 'model_tC', 'model_xA', 'model_xB', 'model_xD']
        var_dic = dict.fromkeys(col_names, 0)

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
        var_dic["mileage"] = mileage
        var_dic["transmission_display"] = gear
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

        # print(teststr)

        car_specs = pd.DataFrame(var_dic, index=[0]).to_numpy().reshape(1,-1)

        price = round(int(myModel.predict(car_specs)))

        # print(str(price))

        # todo: replace the returned value with the predicted price
        # wrap it from numerical to string
        return str(price)
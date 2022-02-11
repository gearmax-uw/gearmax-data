# python -m pip install elasticsearch
# python -m pip install elasticsearch[async]

import csv
import json
from operator import index
import time
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

index_name = 'used-car'

# es vs. db
# index => db
# type => table (depreciated in Elasticsearch 7.0+)
# document => row 
# field => column

# delte mapping

# delete the previous index first
if es.indices.exists(index = 'used-dar'):
    print('index deleted')
    es.indices.delete(index = 'used-car')

# create a index
# index -> database
es.indices.create(index=index_name, ignore=400)

# put mappings set up field types
type_mapping = {
  "properties": {
        "id": {
            "type": "long"
        },
        "back_legroom": {
            "type": "double"
        },
        "body_type": {
            "type": "keyword"
        },
        "city": {
            "type": "keyword"
        },
        "city_fuel_economy": {
            "type": "integer"
        },
        "country": {
            "type": "keyword"
        },
        "engine_displacement": {
            "type": "integer"
        },
        "engine_type": {
            "type": "keyword"
        },
        "exterior_color": {
            "type": "keyword"
        },
        "front_legroom": {
            "type": "double",
        },
        "fuel_tank_volume": {
            "type": "double",
        },
        "fuel_type": {
            "type": "keyword"
        },
        "height": {
            "type": "double"
        },
        "highway_fuel_economy": {
            "type": "integer"
        },
        "interior_color": {
            "type": "keyword"
        },
        "is_depreciated": {
            "type": "boolean"
        },
        "is_new": {
            "type": "boolean"
        },
        "length": {
            "type": "double"
        },
        "listed_date": {
            "type": "date"
        },
        "listing_color": {
            "type": "keyword"
        },
        "main_picture_url": {
            "type": "keyword"
        },
        "major_options": {
            "type": "keyword"
        },
        "make_name": {
            "type": "keyword"
        },
        "maximum_seating": {
            "type": "integer"
        },
        "mileage": {
            "type": "integer"
        },
        "model_name": {
            "type": "keyword"
        },
        "owner_count": {
            "type": "integer"
        },
        "power": {
            "type": "keyword"
        },
        "price": {
            "type": "integer"
        },
        "seller_rating": {
            "type": "double"
        },
        "torque": {
            "type": "keyword"
        },
        "transmission": {
            "type": "keyword"
        },
        "transmission_display": {
            "type": "keyword"
        },
        "trim_name": {
            "type": "keyword"
        },
        "vin": {
            "type": "keyword"
        },
        "wheel_system": {
            "type": "keyword"
        },
        "wheel_system_display": {
            "type": "keyword"
        },
        "wheelbase": {
            "type": "double"
        },
        "width": {
            "type": "double"
        },
        "year": {
            "type": "integer"
        },
        "zip": {
            "type": "keyword"
        }
    }
}

# put field type mapping to es
es.indices.put_mapping(body = type_mapping, index = index_name)

bulk_size = 50000

start_time = time.time()

# open original csv file
with open('used_cars_data.csv', 'r', encoding='UTF-8') as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

    doc_id = 0

    actions = []

    for row in d_reader:

        # city = row['city'].strip() # str
        temp = row['city'].strip().title() # str
        temp = temp.replace(r'-', ' ', regex=True)
        city = temp

        # listing_color = row['listing_color'].replace(' ', '') # str
        temp = row['listing_color'].title()
        temp = temp.replace('Unknown', '')
        temp = temp.replace(' ', '')
        listing_color = temp

        # body_type = row['body_type'].strip() # str
        temp = row['body_type'].strip().title() # str
        temp = temp.replace(r' ', '', regex=True) # remove ' ' in "SUV / crossover"
        temp = temp.replace(r'[/]', ' ', regex=True) # remove '/' in "SUV / crossover"
        body_type =  temp
        
        # make_name = row['make_name'].strip() # str
        temp = row['make_name'].strip().title() # str
        temp = temp.replace(r'-', ' ', regex=True)
        make_name = temp

        # model_name = row['model_name'].strip() # str
        temp = row['model_name'].strip() # str
        temp = temp.replace(r'-', '', regex=True)
        model_name = temp

        # transmission_display = row['transmission_display'].strip() # str
        temp = row['transmission_display'].strip().title() # str
        temp = temp.replace(r'-', ' ', regex=True)
        transmission_display = temp

        # wheel_system_display = row['wheel_system_display'].strip() # str
        temp = row['wheel_system_display'].strip().title() # str
        temp = temp.replace(r'-', ' ', regex=True)
        temp = temp.replace(r'4X2', '4x2', regex=True)
        wheel_system_display = temp

        # fuel_type = row['fuel_type'].strip() # str
        temp = row['fuel_type'].strip().titel() # str
        temp = temp.replace(r'-', ' ', regex=True)
        temp = temp.replace('None', '')
        temp = temp.replace(r' [/] ', '/', regex=True)
        temp = temp.replace(r' [,] ', '/', regex=True)
        fuel_type = temp

        # exterior_color = row['exterior_color'].strip() # str
        temp = row['exterior_color'].strip().title() # str
        temp = temp.replace(r'-', ' ', regex=True)
        temp = temp.replace('None', '')
        exterior_color = temp

        # interior_color = row['interior_color'].strip() # str
        temp = row['interior_color'].strip().title() # str
        temp = temp.replace(r'-', ' ', regex=True)
        temp = temp.replace('None', '')
        temp = temp.replace(r' [/] ', '/', regex=True)
        temp = temp.replace(r' [,] ', '/', regex=True)
        interior_color = temp

        # rename columns
        # car = car.rename(columns={'sp_id': 'seller_id', 'dealer_zip': 'zip', 'power': 'power_rpm', 'torque': 'torque_rpm'})

        # Extract power_rpm
        # power = row['power'].strip() # str
        temp = row['power'].replace(r'.*hp', '', regex=True)
        temp = temp.replace(r'.*@ ', '', regex=True)
        temp = temp.replace(r' RPM', '', regex=True)
        temp = temp.replace(r',', '', regex=True)
        # temp = temp.replace(r'', np.nan, regex=True)
        temp = temp.astype('float')
        power_rpm = temp

        # add torque
        # torque = row['torque'].strip() # str
        temp = row['torque'].strip().replace(r' lb.*', '', regex=True)
        temp = temp.astype('float')
        pound_foot = temp

        # todo: clean/deal with data first
        id = int(doc_id) # int 
        vin = row['vin'].replace(' ', '')  # str 

        
        # if price is null or empty in csv, store null in es (in Python, just assign it None)
        # if not None, store it as int
        d_price = row['price'].replace(' ', '')
        price = int(float(d_price)) if d_price else None # int

        d_year = row['year'].replace(' ', '')
        year = int(d_year) if d_year else None # int


        d_mileage = row['mileage'].replace(' ', '')
        mileage = int(float(d_mileage)) if d_mileage else None # int

        engine_type = row['engine_type'].strip() # str
        
        d_engine_displacement = row['engine_displacement'].replace(' ', '')
        engine_displacement = int(float(d_engine_displacement)) if d_engine_displacement else None # int

        transmission = row['transmission'].strip() # str
        wheel_system = row['wheel_system'].strip() # str
        
        d_wheelbase = row['wheelbase'].replace(' ', '').replace('in', '').replace('-', '')
        wheelbase = float(d_wheelbase) if d_wheelbase else None # float

        d_city_fuel_economy = row['city_fuel_economy'].replace(' ', '')
        city_fuel_economy = int(float(d_city_fuel_economy)) if d_city_fuel_economy else None # int

        d_highway_fuel_economy = row['highway_fuel_economy'].replace(' ', '')
        highway_fuel_economy = int(float(d_highway_fuel_economy)) if d_highway_fuel_economy else None # int
        
        d_fuel_tank_volume = row['fuel_tank_volume'].replace(' ', '').replace('gal', '').replace('-', '')
        fuel_tank_volume = float(d_fuel_tank_volume) if d_fuel_tank_volume else None # float

        
        d_seller_rating = row['seller_rating'].replace(' ', '')
        seller_rating = float(d_seller_rating) if d_seller_rating else None # float

        d_owner_count = row['owner_count'].replace(' ', '')
        owner_count = int(float(d_owner_count)) if d_owner_count else None # int

        trim_name = row['trim_name'].strip() # str

        d_back_legroom = row['back_legroom'].replace(' ', '').replace('in', '').replace('-', '')
        back_legroom = float(d_back_legroom) if d_back_legroom else None # float

        d_front_legroom = row['front_legroom'].replace(' ', '').replace('in', '').replace('-', '')
        front_legroom = float(d_front_legroom) if d_front_legroom else None # float

        d_height = row['height'].replace(' ', '').replace('in', '').replace('-', '')
        height = float(d_height) if d_height else None # float

        d_length = row['length'].replace(' ', '').replace('in', '').replace('-', '')
        length = float(d_length) if d_length else None # float

        d_width = row['width'].replace(' ', '').replace('in', '').replace('-', '')
        width = float(d_width) if d_width else None # float
        
        maximum_seating = None
        if row['maximum_seating'].replace(' ', '').replace('seats', '').replace('-', ''):
            maximum_seating = int()
        
        d_maximum_seating = row['maximum_seating'].replace(' ', '').replace('seats', '').replace('-', '')
        maximum_seating = int(d_maximum_seating) if d_maximum_seating else None # int
        
        listed_date = row['listed_date'].replace(' ', '') # str
        main_picture_url = row['main_picture_url'].replace(' ', '') # str
        is_new = True if row['is_new'] == '1' else False # bool
        zip = row['dealer_zip'].strip() # str
        country = 'US'

        # make major_options a list, es will convert it to Array type when saving it
        major_options = row['major_options'].replace('[', '').replace(']', '').replace('"', '').replace('\'', '').strip().split(",")
        major_options = [x.strip(' ') for x in major_options]

        is_depreciated = False
        if row['frame_damaged'] == '1' or row['has_accidents']  == '1' or row['salvage'] == '1' or row['isCab'] == '1' or row['theft_title'] == '1':
            is_depreciated = True

        # seller info
        # seller_info = {}
        # seller_info['id'] = row['sp_id'].replace(' ', '')
        # seller_info['name'] = row['sp_name'].strip()
        # seller_info['email'] = 
        # seller_info['is_franchise_dealer'] = True if row['franchise_dealer'] == '1' else False

        # depreciation info
        # depreciation_info = None
        # if row['frame_damaged'] == '1' or row['has_accidents']  == '1' or row['salvage'] == '1' or row['isCab'] == '1' or row['theft_title'] == '1':
        #     depreciation_info = {}
        #     depreciation_info['is_frame_damaged'] = True if row['frame_damaged'] == '1' else False
        #     depreciation_info['has_accidents'] = True if row['has_accidents'] == '1' else False
        #     depreciation_info['is_salvaged'] = True if row['salvage'] == '1' else False
        #     depreciation_info['is_cab'] = True if row['isCab'] == '1' else False
        #     depreciation_info['is_theft_title'] = True if row['theft_title'] == '1' else False

        # pickup truck info
        # bed = row['bed'].replace(' ', '')
        # bed_length = row['bed_length'].replace(' ', '').replace('in', '').replace('-', '')
        # cabin = row['cabin'].replace(' ', '')
        # pickup_truck_info = None
        # if body_type == 'Pickup Truck':
        #     pickup_truck_info = {}
        #     pickup_truck_info['bed'] = bed
        #     pickup_truck_info['bed_length'] = bed_length
        #     pickup_truck_info['cabin'] = cabin

        # make a document to be put in es
        car_post = {
            'id': id,
            'vin': vin,
            'make_name': make_name,
            'model_name': model_name,
            'price': price,
            'year': year,
            'mileage': mileage,
            'body_type': body_type,
            'exterior_color': exterior_color,
            'interior_color': interior_color,
            'engine_type': engine_type,
            'engine_displacement': engine_displacement,
            'torque': torque,
            'power': power,
            'transmission': transmission,
            'transmission_display': transmission_display,
            'wheel_system': wheel_system,
            'wheel_system_display': wheel_system_display,
            'wheelbase': wheelbase,
            'city_fuel_economy': city_fuel_economy,
            'highway_fuel_economy': highway_fuel_economy,
            'fuel_tank_volume': fuel_tank_volume,
            'fuel_type': fuel_type,
            'seller_rating': seller_rating,
            'owner_count': owner_count,
            'trim_name': trim_name,
            'back_legroom': back_legroom,
            'front_legroom': front_legroom,
            'height': height,
            'length': length,
            'width': width,
            'maximum_seating': maximum_seating,
            'listed_date': listed_date,
            'listing_color': listing_color,
            'main_picture_url': main_picture_url,
            'is_new': is_new,
            'zip': zip,
            'city': city,
            'country': country,
            'major_options': major_options,
            'is_depreciated': is_depreciated
        }
        
        # actual operatoin to save the document 'car_post' to the index 'used-dar'
        # res = es.index(index='used-car', id=doc_id, document=car_post)

        spec_action = {
            "_index": index_name,
            "_id": doc_id,
            "_source": car_post
        }
        actions.append(spec_action)

        doc_id += 1
        if doc_id != 0 and doc_id % bulk_size == 0:
            # every time, only insert data of bulk_size
            try:
                resp = helpers.bulk(
                    es,
                    actions,
                    index = index_name
                )
                print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))
                actions.clear()
                break
            except Exception as err:
                print("Elasticsearch helpers.bulk() ERROR:", err)

            print("save/update %d car posts" % (doc_id))
            

if len(actions) > 0:
    try:
        resp = helpers.bulk(
            es,
            actions,
            index = index_name
        )
        print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))
        actions.clear()
    except Exception as err:
        print("Elasticsearch helpers.bulk() ERROR:", err)

print("save/update %d car posts" % (doc_id))

print("--- completed in %s seconds ---" % (time.time() - start_time))

        
    
    
        
            
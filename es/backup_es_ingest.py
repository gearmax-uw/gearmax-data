# python -m pip install elasticsearch
# python -m pip install elasticsearch[async]

import csv
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# es vs. db
# index => db
# type => table (depreciated in Elasticsearch 7.0+)
# document => row 
# field => column

# create a index
# index -> database
es.indices.create(index='used-car', ignore=400)

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
        "depreciation_info": {
            "properties": {
                "has_accidents": {
                    "type": "boolean"
                },
                "is_cab": {
                    "type": "boolean"
                },
                "is_frame_damaged": {
                    "type": "boolean"
                },
                "is_salvaged": {
                    "type": "boolean"
                },
                "is_theft_title": {
                    "type": "boolean"
                }
            }
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
        "is_franchise_dealer": {
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
        "main_picture_url": {
            "type": "keyword"
        },
        "major_options": {
            "type": "text"
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
        "pickup_truck_info": {
            "properties": {
                "bed": {
                    "type": "keyword"
                },
                "bed_length": {
                    "type": "double"
                },
                "cabin": {
                    "type": "keyword"
                }
            }
        },
        "power": {
            "type": "keyword"
        },
        "price": {
            "type": "integer"
        },
        "seller_id": {
            "type": "keyword"
        },
        "seller_name": {
            "type": "keyword"
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
            "type": "keyword"
        },
        "width": {
            "type": "integer"
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
es.indices.put_mapping(body = type_mapping, index = 'used-car')

# open original csv file
with open('used_cars_data.csv', 'r', encoding='UTF-8') as f:
    d_reader = csv.DictReader(f)
    headers = d_reader.fieldnames

    doc_id = 0

    for row in d_reader:
        # todo: clean/deal with data first
        id = doc_id
        vin = row['vin'].replace(' ', '')

        make_name = row['make_name'].strip()
        model_name = row['model_name'].strip()
        price = row['price'].strip()
        year = row['year'].strip()
        mileage = row['mileage'].strip()
        body_type = row['body_type'].strip()
        exterior_color = row['exterior_color'].strip()
        interior_color = row['interior_color'].strip()
        engine_type = row['engine_type'].strip()
        engine_displacement = row['engine_displacement'].strip()
        torque = row['torque'].strip()
        power = row['power'].strip()
        transmission = row['transmission'].strip()
        transmission_display = row['transmission_display'].strip()
        wheel_system = row['wheel_system'].strip()
        wheel_system_display = row['wheel_system_display'].strip()
        wheelbase = row['wheelbase'].strip()
        city_fuel_economy =  row['city_fuel_economy'].strip()
        highway_fuel_economy = row['highway_fuel_economy'].strip()
        fuel_tank_volume = row['fuel_tank_volume'].replace(' ', '').replace('gal', '').replace('-', '')
        fuel_type = row['fuel_type'].strip()
        seller_rating = row['seller_rating'].strip()
        owner_count = row['owner_count'].strip()
        trim_name = row['trim_name'].strip()
        back_legroom = row['back_legroom'].replace(' ', '').replace('in', '').replace('-', '')
        front_legroom = row['front_legroom'].replace(' ', '').replace('in', '').replace('-', '')
        height = row['height'].replace(' ', '').replace('in', '').replace('-', '')
        length = row['length'].replace(' ', '').replace('in', '').replace('-', '')
        width = row['width'].replace(' ', '').replace('in', '').replace('-', '')
        maximum_seating = row['maximum_seating'].replace(' ', '').replace('seats', '').replace('-', '')
        listed_date = row['listed_date'].strip()
        main_picture_url = row['main_picture_url'].strip()
        is_new = True if row['is_new'] == '1' else False
        zip = row['dealer_zip'].strip()
        city = row['city'].strip()
        country = 'US'

        # make major_options a list, es will convert it to Array type when saving it
        major_options = row['major_options'].replace('[', '').replace(']', '').replace('"', '').replace('\'', '').strip().split(",")

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
            'seller_id': seller_id, 
            'seller_name': seller_name,
            'is_franchise_dealer': is_franchise_dealer,
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
            'main_picture_url': main_picture_url,
            'is_new': is_new,
            'zip': zip,
            'city': city,
            'country': country,
            'major_options': major_options,
            'depreciation_info': depreciation_info,
            'pickup_truck_info': pickup_truck_info
        }
        
        # actual operatoin to save the document 'car_post' to the index 'used-dar'
        res = es.index(index='used-car', id=doc_id, document=car_post)

        # print(res['result'])

        # res = es.get(index='used-car', id=1)
        # print(res['_source'])

        # res.indices.refresh(index="test-index")

        if doc_id != 0 and doc_id % 10000 == 0:
            print("save/update %d car posts" % (doc_id))
            break
        doc_id += 1
        
            
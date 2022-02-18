# GearMax-Data

### Data Storage and Querying

We use MySQL to store data due to ACID of RDBMS. However, since the data volume is huge (about 3 million) records, the querying speed is significantly slow. To meet the performance requirements, we use Elasticsearch as the complementary of MySQL. When users query, we search data from Elasticsearch. When new data is to be inserted or removed, we update MySQL and Elasticsearch simultaneously.

### Database Schema Design

The design of database schema can be found via this [link](https://dbdiagram.io/d/61dba26bf8370f0a2ee9e2db).

### Elasticsearch Data Modelling Design

The design fo elasticsearch data modelling is listed as below:

```json
{
    "used-car": {
        "aliases": {},
        "mappings": {
            "properties": {
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
                    "type": "double"
                },
                "fuel_tank_volume": {
                    "type": "double"
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
                "id": {
                    "type": "long"
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
        },
        "settings": {
            "index": {
                "creation_date": "1643726975666",
                "number_of_shards": "1",
                "number_of_replicas": "1",
                "uuid": "wC8vaStGTDiPvetNDrzCJQ",
                "version": {
                    "created": "7060299"
                },
                "provided_name": "used-car"
            }
        }
    }
}
```

### Data Field Requirements

For the storage in MySQL, we do not allow null value for string type but we do allow the empty value such as ''. For other data types, we do allow null values.

For the data fomatting, we require:

- Assume the data can be splited into multiple words, then the first character of each word is captalized (uppercase) while the remaining ones are lowercase.
- Use one space between each word. Do not allow any other symbols to connect words.
- No space before the first word and last word. 

As developers, we require all columns listed below follow the specific data format. For the columns not mentioned, we do not force the data manipulation.

- city
- make_name
- model_name
- body_type
- listing_color
- interior_color (None => '' + remove spaces in ())
- exterior_color
- transmission_display
- wheel_system
- fuel_type

### How to put data of Used Car Dataset to Elasticsearch?

1. Make sure you have Elasticsearch service running locally. It can be Docker service or the installed Elasticsearch program.
2. Make sure the port 9200 of ES is exposed.
3. Go to the directory `gearmax-data/es/` and ensure that `used_cars_data.csv` locates in the same direcory. The dataset can be downloaded from [Kaggle US Used Dataset](https://www.kaggle.com/ananaymital/us-used-cars-dataset).
4. run `python ingest_es_data.py` or `python3 ingest_es_data.py`, then all data will be saved to your ES server.

**Note:** If you don't want to save all of the data from the csv file to your ES server, comment out `break` in `ingest_es_data.py`. Then only `bulk_size` (in our case, 50000) docs (rows in SQL) will be saved. 

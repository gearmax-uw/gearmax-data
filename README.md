# GearMax-Data

### Database Schema Design

### Elasticsearch Data Modelling Design

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




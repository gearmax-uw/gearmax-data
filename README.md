# gearmax-data

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




DROP TABLE IF EXISTS car;

select '-----------------------------------------------------------------' as '';
select 'Create car' as '';

create table if not exists car (
			id int NOT NULL primary key,
            vin varchar(22),
            is_depreciated varchar(5),
            seller_id int,
            zip int, 
            city varchar(19), 
            country varchar(20), 
            price float, 
            year int, 
            make_name varchar(13), 
            model_name varchar(25), 
            body_type varchar(15), 
            maximum_seating int, 
            listing_color varchar(20),
            interior_color varchar(50), 
            exterior_color varchar(50), 
            mileage float, 
            length float, 
            width float, 
            height float, 
            wheelbase float, 
            front_legroom float, 
            back_legroom float, 
            engine_displacement float, 
            engine_type varchar(20), 
            transmission varchar(11), 
            transmission_display varchar(34), 
            wheel_system varchar(3), 
            wheel_system_display varchar(17), 
            horsepower float, 
            power_rpm int, 
            pound_foot int, 
            torque_rpm int, 
            fuel_tank_volume float, 
            fuel_type varchar(17), 
            city_fuel_economy float, 
            highway_fuel_economy float, 
            is_new boolean, 
            listed_date varchar(10), 
            main_picture_url varchar(167), 
            owner_count int, 
            seller_rating float, 
            trim_name varchar(81) 
			-- index (body_type),
			-- index (price),
			-- index (owner_count)
		  );

load data infile 'test_data/car.csv' ignore into table car
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 
    (id, vin, is_depreciated, seller_id, zip, city, country, price, year, make_name, model_name, 
            body_type, maximum_seating, listing_color, interior_color, exterior_color, 
            mileage, length, width, height, wheelbase, front_legroom, back_legroom, engine_displacement, 
            engine_type, transmission, transmission_display, wheel_system, wheel_system_display, 
            horsepower, power_rpm, pound_foot, torque_rpm, fuel_tank_volume, fuel_type, city_fuel_economy, 
            highway_fuel_economy, @is_new, listed_date, main_picture_url, owner_count, seller_rating, trim_name)
    set is_new = (@is_new = 'True');
        -- has_accidents = (@has_accidents = 'True'),
        -- salvage = (@salvage = 'True'),
        -- is_cab = (@is_cab = 'True'),
        -- theft_title = (@theft_title = 'True');
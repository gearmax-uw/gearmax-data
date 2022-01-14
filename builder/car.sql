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
            body_type varchar(13), 
            maximum_seating int, 
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
            is_new varchar(5), 
            listed_date varchar(10), 
            main_picture_url varchar(167), 
            owner_count int, 
            seller_rating float, 
            trim_name varchar(81) 
			-- index (body_type),
			-- index (price),
			-- index (owner_count)
		  );

load data infile '/tmp/ece651/debug/Car.csv' ignore into table car
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 

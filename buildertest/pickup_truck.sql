DROP TABLE IF EXISTS pickup_truck;

select '-----------------------------------------------------------------' as '';
select 'Create pickup_truck' as '';

create table if not exists pickup_truck(
			id int NOT NULL primary key,
            bed varchar(7),
            bed_length float,
            cabin varchar(12)
            );

load data infile 'test_data/mini_data/pickup_truck.csv' ignore into table pickup_truck
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 


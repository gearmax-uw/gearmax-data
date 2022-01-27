DROP TABLE IF EXISTS car_option;

select '-----------------------------------------------------------------' as '';
select 'Create car_option' as '';

create table if not exists car_option(
			option_id int,
            car_id int
            );

load data infile 'test_data/mini_data/car_option.csv' ignore into table car_option
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 


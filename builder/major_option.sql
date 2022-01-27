DROP TABLE IF EXISTS pickup_truck;

select '-----------------------------------------------------------------' as '';
select 'Create major_option' as '';

create table if not exists major_option(
			option_id int NOT NULL primary key,
            option varchar(40)
            );

load data infile 'test_data/major_option.csv' ignore into table major_option
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 


DROP TABLE IF EXISTS depreciation_info;

select '-----------------------------------------------------------------' as '';
select 'Create depreciation_info' as '';

create table if not exists depreciation_info(
			id int NOT NULL primary key,
            frame_damaged varchar(5),
            has_accidents varchar(5),
            salvage varchar(5),
            isCab varchar(5),
            theft_title varchar(5)
            );

load data infile '/tmp/ece651/debug/depreciation_info.csv' ignore into table depreciation_info
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 


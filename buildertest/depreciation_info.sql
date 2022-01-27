DROP TABLE IF EXISTS depreciation_info;
  
select '-----------------------------------------------------------------' as '';
select 'Create depreciation_info' as '';

create table if not exists depreciation_info(
            id int NOT NULL primary key,
            frame_damaged boolean,
            has_accidents boolean,
            salvage boolean,
            is_cab boolean,
            theft_title boolean
            );

load data infile 'test_data/mini_data/depreciation_info.csv' ignore into table depreciation_info
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines
    (id, @frame_damaged, @has_accidents, @salvage, @is_cab, @theft_title)
    set frame_damaged = (@frame_damaged = 'True'),
        has_accidents = (@has_accidents = 'True'),
        salvage = (@salvage = 'True'),
        is_cab = (@is_cab = 'True'),
        theft_title = (@theft_title = 'True');
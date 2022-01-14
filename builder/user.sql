DROP TABLE IF EXISTS user;

select '-----------------------------------------------------------------' as '';
select 'Create user' as '';

create table if not exists user(
			id int NOT NULL primary key,
            name varchar(128),
            email varchar(255),
            type varchar(10),
            is_franchise_dealer varchar(5)
            );

load data infile '/tmp/ece651/debug/user.csv' ignore into table user
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 


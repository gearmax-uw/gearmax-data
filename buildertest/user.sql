DROP TABLE IF EXISTS user;

select '-----------------------------------------------------------------' as '';
select 'Create user' as '';

create table if not exists user(
			id int NOT NULL primary key,
            name varchar(128),
            email varchar(255),
            type varchar(10),
            is_franchise_dealer boolean
            );

load data infile 'test_data/user.csv' ignore into table user
-- load data infile '/tmp/Car.csv' ignore into table car
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines 
    (id, name, email, type, @is_franchise_dealer)
    set is_franchise_dealer = (@is_franchise_dealer = 'True');


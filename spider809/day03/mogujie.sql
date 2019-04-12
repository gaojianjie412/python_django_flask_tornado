create database mogujie9 default character set=utf8;

use mogujie9;

create table products (
    id integer auto_increment primary key,
    trade_item_id varchar(128),
    item_type varchar(32),
    img varchar(1024),
    client_url varchar(1024),
    link varchar(1024),
    title varchar(512),
    orgprice varchar(32),
    price varchar(32)
);
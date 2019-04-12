create database xiami default character set=utf8;

use xiami;

create table mp3 (
    id integer atuo_increment primary key,
    title varchar(128),
    img varchar(512),
    lrc varchar(1024)
);
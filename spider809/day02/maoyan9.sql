create database maoyan9 default character set=utf8;

use maoyan9;

create table movie (
    id integer primary key auto_increment,
    movie_name varchar(256),
    actor varchar(256),
    releasetime varchar(256),
    cover_url varchar(1024),
    score varchar(32),
    rank varchar(32),
    detail_url varchar(1024)
);

create unique index ux_movie_movie_name on movie(movie_name)

create index ix_movie_actor on movie(actor);
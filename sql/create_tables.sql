create table users (
    id int primary key not null,
    email varchar(50) not null,
    first_name varchar(50),
    last_name varchar(50),
    level int default 0
);
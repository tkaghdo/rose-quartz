
create table users (
    id int primary key not null,
    email varchar(50) not null UNIQUE,
    name varchar(50),
    password varchar(50),
    level int default 0
);

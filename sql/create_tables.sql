
-- this is a legacy table
create table users (
    id int primary key not null,
    email varchar(50) not null UNIQUE,
    name varchar(50),
    password varchar(50),
    level int default 0
);


create table dim_user(
  user_id int primary key not null,
  email varchar(50) not null UNIQUE,
  name varchar(50) not null,
  password varchar(50) not null,
  date_created date,
  date_updated date,
  last_login date,
  quests varchar(1000) -- this is a pipe delimeted field with the languages the user is enrolled in
);

create table dim_language(
  language_id int primary key not null,
  language varchar(50) not null
);

create table dim_question(
  question_id int primary key not null,
  question varchar(3000) not null
);

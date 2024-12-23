create database mini_project;
use mini_project;
CREATE TABLE admindetails (
    User_Name VARCHAR(255),
    PASS_WORD VARCHAR(255) PRIMARY KEY
);

INSERT INTO admindetails (User_Name, PASS_WORD) VALUES ('sam', 'password123');
INSERT INTO admindetails (User_Name, PASS_WORD) VALUES ('shreya', 'pw456');
INSERT INTO admindetails (User_Name, PASS_WORD) VALUES ('cs', 'mypw');
INSERT INTO admindetails (User_Name, PASS_WORD) VALUES ('sinch', 'pw7');
INSERT INTO admindetails (User_Name, PASS_WORD) VALUES ('yogi', 'pw89');


create table student (
Name varchar(20),
Branch varchar(20),
USN varchar(20),
Section varchar (2)
);

alter table student add column ImagePath varchar(255);

drop table student;
show tables;
select * from student;
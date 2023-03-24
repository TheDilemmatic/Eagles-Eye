
CREATE DATABASE cbse_compsci_proj;
USE cbse_compsci_proj;
CREATE TABLE employee_details
(
employee_code CHAR(10) NOT NULL PRIMARY KEY,
employee_name CHAR(20) NOT NULL,
gender CHAR(10),
department char(20) NOT NULL,
post_held char(20) NOT NULL,
salary INT(10) DEFAULT 30000,
phone INT(10) NOT NULL,
e_mail CHAR(20) NOT NULL,
qualification TEXT,
achievements TEXT,
experience TEXT,
ratings TEXT
);
DESC employee_details;
SELECT * FROM employee_details;

create_teacher_table = """
create table teacher(
teacher_id int primary key,
first_name varchar(100) not null,
last_name varchar(100) not null,
language_1 varchar(3) not null,
dob date,
tax_id int unique,
phone_number varchar(30)
);
"""
create_client_table = """
create table client(
client_id int primary key,
client_name varchar(50) not null,
address varchar(100) not null,
industry varchar(30) not null
);
"""
create_participant_table = """
CREATE TABLE participant (
participant_id INT PRIMARY KEY,
first_name VARCHAR(40) NOT NULL,
last_name VARCHAR(40) NOT NULL,
phone_no VARCHAR(20),
client INT
);
"""
create_course_table = """
CREATE TABLE course (
course_id INT PRIMARY KEY,
course_name VARCHAR(40) NOT NULL,
language VARCHAR(3) NOT NULL,
level VARCHAR(2),
course_length_weeks INT,
start_date DATE,
in_school BOOLEAN,
teacher INT,
client INT
);
"""
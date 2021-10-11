import pymysql
import os

conn = pymysql.connect(
    user=os.getenv('USER_DATABASE'),
    password=os.getenv('PASSWORD_DATABASE'),
    autocommit=True,
)

sql = conn.cursor()

create_students = '''
insert into students values
('Jaedson','2007-08-02', 'A', 'B'),
('Luiz','2005-03-11', 'D', 'B'),
('Pedro','2002-04-19', 'R', 'C'),
('Arlete','1996-02-21', 'R', 'A'),
('Murilo','2004-08-08', 'D', 'B'),
('Arthur','2008-09-26', 'A', 'C'),
('Lucas','2009-01-09', 'A', 'A'),
('Adréia','2007-08-02', 'A', 'B'),
('João','2005-03-11', 'D', 'B'),
('Lívia','2002-04-19', 'R', 'C'),
('Vítoria','1996-02-21', 'R', 'A'),
('Kauã','2004-08-08', 'D', 'B'),
('Sheila','2008-09-26', 'A', 'C'),
('Nicolas','2009-01-09', 'A', 'A'),
('Laura','2007-08-02', 'A', 'B'),
('Gustavo','2005-03-11', 'D', 'B'),
('Ana','2002-04-19', 'R', 'C'),
('Júlia','1996-02-21', 'R', 'A'),
('Maria','2004-08-08', 'D', 'B'),
('Gabriel','2008-09-26', 'A', 'C'),
('Bruno','2009-01-09', 'A', 'A')
'''

sql.execute('create database if not exists school')
sql.execute('use school')
sql.execute('drop table if exists students')
sql.execute('create table if not exists students(name varchar(20), birth date, status char(1), room char(1))')
sql.execute(create_students)


class MySQL:
    def __init__(self) -> None:
        conn.ping()

    def return_student(self, name: str) -> tuple:
        sql.execute('select * from students where lower(name) like concat("%%",%s,"%%")', (name,))
        student = sql.fetchall()

        print(student)
        return student

school = MySQL()
school.return_student('jae')
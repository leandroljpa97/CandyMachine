drop table if exists quiz;
drop table if exists highscore;

create table quiz(
id integer,
question varchar(255),
correct_answer varchar(255),
answer2 varchar(255),
answer3 varchar(255),
answer4 varchar(255),
primary key(id)
);

create table highscore(
name varchar(255),
course varchar(255),
id varchar(255),
mail varchar(255),
seconds_time numeric(5,2),
correct_answer integer,
total_questions integer);





insert into quiz values (1,'Quem foi o primeiro rei de Portugal?','D.Afonso Henriques','D. Manuel |',' D.João', 'D. Afonso |');
insert into quiz values (2,'Qual instrução serve para fazer um ciclo','while','if',' case', 'print');
insert into quiz values (3,'Qual instrução serve para fazer um ciclo','nenhuma das anteriores','if',' case', 'print');
insert into quiz values (4,'Qual instrução serve para fazer um ciclo','for','if',' case', 'print');
insert into quiz values(5,'Quem descobriu a india?','Vasco da Gama','D.Manuel I','Infante Dom Henriques', 'D.Pedro V');
insert into quiz values(6,'No mandato de quem é que se descobriu a india?','D.Manuel I','Vasco da Gama','Infante Dom Henriques', 'D. Pedro V');
insert into quiz values(7,'Para que serve o SSH','aceder remotamente a outro computador','ter seguro de que a mensagem chegou ao destino','fazer scripts','x');
drop table if exists quiz;
drop table if exists highscore;

create table quiz(
id integer,
question varchar(255),
answer1 varchar(255),
answer2 varchar(255),
answer3 varchar(255),
answer4 varchar(255),
correct_answer integer,
primary key(id));

create table highscore(
name varchar(255),
course varchar(255),
id varchar(255),
mail varchar(255),
seconds_time numeric(5,2),
correct_answer integer,
total_questions integer);





insert into quiz values (1,'Quem foi o primeiro rei de Portugal?','D.Afonso Henriques','D. Manuel I',' D.João', 'D. Afonso I',1);
insert into quiz values (2,'Qual instrução serve para fazer um ciclo','if','case','while', 'print',3);
insert into quiz values (3,'Qual instrução serve para fazer um ciclo','if','case', 'print','nenhuma das anteriores',4);
insert into quiz values (4,'Qual instrução serve para fazer um ciclo','for','if',' case', 'print',1);
insert into quiz values(5,'Quem descobriu a Índia?','D.Manuel I','Vasco da Gama','Infante Dom Henriques', 'D.Pedro V',2);
insert into quiz values(6,'No mandato de quem é que se descobriu a Índia?','Vasco da Gama','D.Manuel I','Infante Dom Henriques', 'D. Pedro V',2);
insert into quiz values(7,'Para que serve o SSH','ter seguro de que a mensagem chegou ao destino','aceder remotamente a outro computador','fazer scripts','fazer ciclos',2);
insert into quiz values (8,'Qual a fruta que atingiu Isaac Newtown na cabeça quando este criou a lei da gravitação universal?','Pêra','Laranja', 'Maçã','Banana',3);
insert into quiz values (9,'300000000 m/s é a velocidade de que partícula no vácuo?','Neutrão','Protão','Eletrão', 'Fotão',4);
insert into quiz values (10,'Qual é a 1ª Lei de Newton?','Lei fundamental da dinâmica','Princípio da ação e reação','Princípio da inércia', 'Relatividade Geral',3);
insert into quiz values (11,'Qual é a 2ª Lei de Newton?',' Lei fundamental da dinâmica','Princípio da inércia','Relatividade Geral', 'Princípio da ação e reação',1);
insert into quiz values (12,'Qual é a 3ª Lei de Newton?','Princípio da inércia','Lei fundamental da dinâmica','Relatividade Geral','Princípio da ação e reação',4);
insert into quiz values (13,'Que físico desenvolveu a teoria da relatividade geral?','Niels Bohr','Isaac Newton','Albert Einstein', 'Joseph John Thomson',3);
insert into quiz values (14,'O gato de Schrödinger está?','Morto','Nenhuma das anteriores', 'Vivo', 'Com fome',2);
insert into quiz values (15,'Qual a força fundamental mais forte?','Força nuclear fraca','Força nuclear forte', 'Gravidade', 'Força Eletromagnética',2);
insert into quiz values (16,'Qual a força fundamental mais fraca?','Gravidade','Força nuclear fraca','Força Eletromagnética', 'Força nuclear forte',1);
insert into quiz values (17,'Qual é o único ramo da física que é indeterminista?','Eletromagnetismo','Termodinâmica','Mecânica quântica', 'Óptica e ondas',3);
insert into quiz values (18,'Quem é o autor do livro "A Brief History of Time "?','Walter Lewin','Peter Higgs','Isaac Newton','Stephen Hawking',4);
insert into quiz values (19,'Quem é o apresentador da série "Cosmos" apresentada em 1980?','Stephen Hawking','Carl Sagan', 'Neil deGrasse Tyson', 'Alan Guth',2);
insert into quiz values (20,'Quem é o apresentador da série americana "Cosmos: A Spacetime Odyssey"?','Alan Guth','Carl Sagan','Neil deGrasse Tyson', 'Stephen Hawking',3);
insert into quiz values (21,'Qual planeta do Sistema Solar tem os dias mais curtos?','Marte','Saturno','Júpiter','Mercúrio',3);
insert into quiz values (22,'Que planetas do Sistema Solar são conhecidos por "gigantes gelados"?','Mercúrio e Vénus','Júpiter e Saturno','Terra e Marte','Urano e Neptuno',4);
insert into quiz values (23,'Qual destes planetas é um gigante gasoso?','Saturno','Vénus','Marte','Mercúrio',1);
insert into quiz values (24,'Qual destas empresas desenvolveu o "Falcon Heavy"?','Boeing','Blue Origin','Virgin Galactic','SpaceX',4);
insert into quiz values (25,'Qual o nome do primeiro chimpanzé lançado para o espaço em 1961?','Dezik','Albert II','Ham', 'Hector',3);
insert into quiz values (26,'Qual o nome do primeiro ser vivo a orbitar o planeta Terra?','Belka','Laika','Sally', 'Strelka',2);
insert into quiz values (27,'Que planeta no Sistema Solar tem o eixo de rotação inclinado 98º?','Urano','Vénus','Júpiter','Saturno',1);
insert into quiz values (28,'Mimas, Dione e Titã são luas de que planeta?','Júpiter','Saturno','Neptuno', 'Urano',2);
insert into quiz values (29,'Ceres é um planeta anão, entre que planetas órbita?','Proxima Centauri a e Proxima Centauri b','Saturno e Urano','Marte e Júpiter', 'Júpiter e Saturno',3);
insert into quiz values (30,'Quantos planetas no Sistema Solar têm luas?','7','6','4', '5',2);
-- insert into quiz values (31,'','','',' ', '');
-- insert into quiz values (32,'','','',' ', '');
-- insert into quiz values (33,'','','',' ', '');
-- insert into quiz values (34,'','','',' ', '');
-- insert into quiz values (35,'','','',' ', '');
-- insert into quiz values (36,'','','',' ', '');
-- insert into quiz values (37,'','','',' ', '');
-- insert into quiz values (38,'','','',' ', '');
-- insert into quiz values (39,'','','',' ', '');
-- insert into quiz values (40,'','','',' ', '');
-- insert into quiz values (41,'','','',' ', '');
-- insert into quiz values (42,'','','',' ', '');
-- insert into quiz values (43,'','','',' ', '');
-- insert into quiz values (44,'','','',' ', '');
-- insert into quiz values (45,'','','',' ', '');
-- insert into quiz values (46,'','','',' ', '');
-- insert into quiz values (47,'','','',' ', '');
-- insert into quiz values (48,'','','',' ', '');
-- insert into quiz values (49,'','','',' ', '');
-- insert into quiz values (50,'','','',' ', '');

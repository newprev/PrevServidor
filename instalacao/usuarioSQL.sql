/*Script criado por Israel Alves Lucena Gomes em 30/04/2023*/


/* Criação do usuário */
CREATE USER 'NEWPREV'@'localhost' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
CREATE USER 'NEWPREV'@'%.%.%.%' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
CREATE USER 'NEWPREV'@'%' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
CREATE USER 'NEWPREV'@'0' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
CREATE USER 'NEWPREV'@'0.0.0.0' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';

/* Concedendo privilégios */
GRANT ALL PRIVILEGES ON *.* TO 'NEWPREV'@'localhost';

/* Reiniciando */
FLUSH PRIVILEGES;
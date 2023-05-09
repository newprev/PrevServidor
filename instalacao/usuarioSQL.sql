/*Script criado por Israel Alves Lucena Gomes em 30/04/2023*/

USE GIDEON;

DROP PROCEDURE IF EXISTS concedePermissoes;

/*DELIMITER //*/
CREATE PROCEDURE concedePermissoes ()
	
	BEGIN
		DECLARE usuarioExiste  BOOL;
		
		SELECT TRUE INTO usuarioExiste FROM mysql.user WHERE user = 'NEWPREV' LIMIT 1; 

		/*Caso os usuários já existam*/
		IF usuarioExiste = 1 THEN 
			DROP USER IF EXISTS 'NEWPREV'@'localhost';
			DROP USER IF EXISTS 'NEWPREV'@'%.%.%.%';
			DROP USER IF EXISTS 'NEWPREV'@'%';
			DROP USER IF EXISTS 'NEWPREV'@'0';
			DROP USER IF EXISTS 'NEWPREV'@'0.0.0.0';
		END IF;
		
		/* Criação do usuário */
		CREATE USER 'NEWPREV'@'localhost' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
		CREATE USER 'NEWPREV'@'%.%.%.%' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
		CREATE USER 'NEWPREV'@'%' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
		CREATE USER 'NEWPREV'@'0' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
		CREATE USER 'NEWPREV'@'0.0.0.0' IDENTIFIED WITH mysql_native_password BY '__NewPrev2021__';
	
		/* Concedendo privilégios */
		GRANT ALL PRIVILEGES ON *.* TO 'NEWPREV'@'localhost';
		GRANT SELECT, UPDATE, INSERT, DELETE ON *.* TO 'NEWPREV'@'%.%.%.%';
		GRANT SELECT, UPDATE, INSERT, DELETE ON *.* TO 'NEWPREV'@'%';
		GRANT SELECT, UPDATE, INSERT, DELETE ON *.* TO 'NEWPREV'@'0';
		GRANT SELECT, UPDATE, INSERT, DELETE ON *.* TO 'NEWPREV'@'0.0.0.0';
		
		/* Reiniciando */
		FLUSH PRIVILEGES;
		
END; //

CALL concedePermissoes();
	

/*DELIMITER ;*/
/*Script criado por Israel Alves Lucena Gomes em 30/04/2023*/

USE GIDEON;
CREATE FUNCTION avaliaUsuario ()

BEGIN

	IF EXISTS (
				SELECT 
					1
				FROM
					mysql.user
				WHERE
					user = 'NEWPREV'
			  ) 
	THEN
	
		DROP USER 'NEWPREV'@'localhost';
		DROP USER 'NEWPREV'@'%.%.%.%';
		DROP USER 'NEWPREV'@'%';
		DROP USER 'NEWPREV'@'0';
		DROP USER 'NEWPREV'@'0.0.0.0';
	
	ELSE
	
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
	
	END IF;
	
	RETURN;

END;
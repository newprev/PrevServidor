#!/bin/bash

FIRST_PARAM="$1"
SENHA="$2"
MANUAL="""
Ajuda para ações comuns na instalação do NewPrev.

-h                           Apresenta opções de ajuda
--help 

--lib-port <senha su>        Parâmetro para liberar a porta do banco de dados para acesso fora do localhost
--fix-mysql 				 Ajusta erro Mysql(Mariadb) no Ubuntu 
--cria-usuario-sql           Roda o script que cria o usuário NEWPREV no banco e dá as permissões necessárias
"""


case $FIRST_PARAM in
	"-h")
		echo "$MANUAL"
	;;

	"--help")
		echo "$MANUAL"
	;;

	"--lib-port")
		echo -e "$SENHA" | sudo -S ufw allow 3306
	;;

	"--fix-mysql")
		sudo -S apt-get install python3-dev default-libmysqlclient-dev build-essential -y
		pip install --upgrade pip
	;;

	"--cria-usuario-sql")
		sudo -S mysql usuarioSQL.sql
esac

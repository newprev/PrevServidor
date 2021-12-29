##Parâmetros importantes
PASSWORD=senha

##Iniciar o servidor
run-dev:
	@python manage.py runserver


## @ Limpeza de migrações
clearAllMigrations: ## Exclui todos os arquivos de migração gerados pelo sistema
	@echo 'Limpando as migrações'
	@rm -f apps/advogado/migrations/*.py && echo "---> apps/advogado/migrations"
	@rm -f apps/escritorios/migrations/*.py && echo "---> apps/escritorios/migrations"
	@rm -f apps/ferramentas/migrations/*.py && echo "---> apps/ferramentas/migrations"
	@rm -f apps/informacoes/migrations/*.py && echo "---> apps/informacoes/migrations"
	@rm -f apps/sincron/migrations/*.py && echo "---> apps/sincron/migrations"
	@rm -f apps/sincron/migrations/*.py && echo "---> apps/newMails/migrations"



recriaAllMigrations: clearAllMigrations makeAllMigrations ## Exclui todos os arquivos de migração, recria todos e completa todas as migrações
deletaRecriaAtualiza: recriaBanco clearAllMigrations makeAllMigrations updateDB-Backup run-dev ## Deleta banco de dados, recria, deleta todos os arquivos de migração, recria, completa a migração,  popula o banco com o último backup feito e reinicia o servidor.


## @ Migracoes
makeAllMigrations: ## Cria todos os arquivos de migração e completa a migração
	@echo 'Makemigrations'
	@python manage.py makemigrations advogado
	@python manage.py makemigrations escritorios
	@python manage.py makemigrations ferramentas
	@python manage.py makemigrations informacoes
	@python manage.py makemigrations sincron
	@python manage.py makemigrations newMails
	@python manage.py migrate


## @ Banco de dados
updateDB-Backup: ## Atualiza o banco baseado nos arquivos de backup criados 
	@echo 'Atualizando todas as tabelas'
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/carenciasLei91.sql
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/convMon.sql
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/expectativaSobrevida.sql
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/indicadores.sql
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/salarioMinimo.sql
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/tetosPrev.sql
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/indicesAtuMonetaria.sql

updateDB-Tabela: ## Atualiza apenas uma tabela baseado no arquivo de backup criado
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" GIDEON < ../backup/indicesAtuMonetaria.sql

recriaBanco: ## Deleta o banco GIDEON, recria o banco e apresenta os bancos criados nessa base
	@mysql -h localhost -u NEWPREV -p"${PASSWORD}" -e "DROP DATABASE GIDEON; CREATE DATABASE GIDEON; SHOW DATABASES;"

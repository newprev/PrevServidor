run-dev:
	python manage.py runserver

clearAllMigrations:
	@echo 'Limpando o cache'
	@rm -f apps/advogado/migrations/*.py && echo "---> apps/advogado/migrations"
	@rm -f apps/escritorios/migrations/*.py && echo "---> apps/escritorios/migrations"
	@rm -f apps/ferramentas/migrations/*.py && echo "---> apps/ferramentas/migrations"
	@rm -f apps/informacoes/migrations/*.py && echo "---> apps/informacoes/migrations"
	@rm -f apps/sincron/migrations/*.py && echo "---> apps/sincron/migrations"

makeAllMigrations:
	@echo 'Makemigrations'
	@python manage.py makemigrations advogado
	@python manage.py makemigrations escritorios
	@python manage.py makemigrations ferramentas
	@python manage.py makemigrations informacoes
	@python manage.py makemigrations sincron

updateDatabases:
	@echo 'Atualizando todas as tabelas'
	@mysql -h localhost -u NEWPREV -p"_NewPrev2021_" GIDEON < ../backup/carenciasLei91.sql
	@mysql -h localhost -u NEWPREV -p"_NewPrev2021_" GIDEON < ../backup/convMon.sql
	@mysql -h localhost -u NEWPREV -p"_NewPrev2021_" GIDEON < ../backup/expectativaSobrevida.sql
	@mysql -h localhost -u NEWPREV -p"_NewPrev2021_" GIDEON < ../backup/indicadores.sql
	@mysql -h localhost -u NEWPREV -p"_NewPrev2021_" GIDEON < ../backup/salarioMinimo.sql
	@mysql -h localhost -u NEWPREV -p"_NewPrev2021_" GIDEON < ../backup/tetosPrev.sql

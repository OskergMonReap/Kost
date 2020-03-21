SHELL := /bin/sh

DEV=docker-compose -f dev-compose.yml -H "ssh://oskr_grme@192.168.8.200"

dev-deploy: ## Deploy containers via dev-compose.yml file
	@echo ''
	@echo '- - - -     Deploying via docker compose    - - - -'
	@echo ''
	@echo '- - - - Building Images starting containers - - - -'
	@echo ''
	$(DEV) up -d --build
	@echo ''
	@echo '- - - -   Containers succesfully started    - - - -'
	@echo '- - - -     Starting django migrations      - - - -'
	@echo ''
	$(DEV) run web python manage.py makemigrations --noinput
	$(DEV) run web python manage.py migrate --noinput
	$(DEV) run web python manage.py migrate --run-syncdb --noinput
	@echo ''
	@echo '- - - -   Migrations succesfully completed  - - - -'
	@echo '- - - -        Collecting some static       - - - -'
	@echo ''
	$(DEV) run web python manage.py collectstatic --noinput
	@echo ''
	@echo '- - - - Static assets collected succesfully - - - -'
	@echo '- - - -       Deployment is completed       - - - -'
	@echo ''
	@echo Development URL: http://192.168.8.200:8000

dev-cleanup: ## Teardown application, remove volumes for clean env
	@echo ''
	@echo '- - - - Stopping/Removing Containers and removing Volumes - - - -'
	@echo ''
	$(DEV) down -v
	@echo ''
	@echo '- - - - Teardown complete. Environment is clean for new build. - - - -'
	@echo ''

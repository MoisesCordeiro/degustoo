clean:
		find . -name "*.pyc" -exec rm -rf {} \;
run: clean
	python manage.py runserver

migrate:
		python manage.py migrate

migrations:
		python manage.py makemigrations

user:
	python manage.py createsuperuser

shell: clean
	python manage.py shell

exclude_migrations: clean
	rm **/migrations/[0-9]*.py

migrate_production:
	python manage.py migrate --settings=degustoo.settings_production

collect_static:
	python manage.py collectstatic

initial_deploy:
	#cap production setup:install_requirements_server
	cap production deploy
	#cap production setup:create_folders
	cap production setup:install_requirements
	cap production setup:conf_files
	cap production setup:migrations
	cap production setup:collect_static
	cap production setup:restart_app

deploy:
	cap production deploy
	cap production setup:install_requirements
	cap production setup:migrations
	cap production setup:collect_static
	cap production setup:restart_app

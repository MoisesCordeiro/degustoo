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
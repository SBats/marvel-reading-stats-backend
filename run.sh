
docker start mrs-postgres

env/bin/python src/manage.py migrate
env/bin/python src/manage.py runserver


if docker inspect mrs-postgres 2>&1 > /dev/null; then
    docker start mrs-postgres
else
    docker run --name mrs-postgres -p 5432:5432 -d postgres
fi

virtualenv -p python3 env
env/bin/pip install -e src
env/bin/python src/manage.py migrate

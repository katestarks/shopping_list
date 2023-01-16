# shopping_list
Keep all of those to-buy items in one place

## Getting started
Prequiste: Docker installation

Run `docker compose up -d --build`
This will create the images needed by the docker container.

Run `docker compose up`
Your docker container has started

Run `docker compose exec web python manage.py migrate`
This command applies the database structure to your database. Because there is no shared database, the app won't run without this.

Navigate to http://127.0.0.1:8000/your_list/. The app should automatically reload if you change any of the source files.

Note, when running docker compse up, there is a built-in delay before the web container starts to allow the db to start up

To stop it run docker-compose stop.

When using docker, run django development commands by prefixing those commands with:
docker compose exec web <django command here>

for example, to run tests:
docker compose exec web python manage.py test your_list
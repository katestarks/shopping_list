# shopping_list
Keep all of those to-buy items in one place

Prequiste: Docker installation

Run docker-compose up -d for a dev server. Navigate to http://127.0.0.1:8000/your_list/. The app should automatically reload if you change any of the source files.

Note, there is a built-in delay before the web container starts to allow the db to start up

To stop it run docker-compose stop.

When using docker, run django development commands by prefixing those commands with:
docker compose exec web <django command here>

for example, to run tests:
docker compose exec web python manage.py test your_list
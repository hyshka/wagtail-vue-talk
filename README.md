# wagtail-gridsome

A trimmed down, revised fork of https://github.com/hyshka/wagtail-vue-talk

In this version, we have switched the original plan Vue.js frontend for Gridsome, a .

The Django server will run on port `8000`, and the Node.js server compiling the Vue.js app will run on port `8080`.

To access the Wagtail admin go to http://localhost:8000/admin/, login is `demo` / `demo123`.

The frontend app is expecting a GraphQL API to be available at `localhost:8000/graphql`.

The regular Django API is available at `localhost:8000/api/v2/`.

```
# build image and start containers
make up

# enter backend (python) container
make enter

# initialize database (inside container)
django-admin.py migrate
django-admin.py createsuperuser

# start django server (inside container)
django-admin.py runserver 0.0.0.0:8000

# ..or use the handy aliases:
djm
djr

# enter frontend (Gridsome) container
make frontend

# start node server (inside container)
gridsome develop

# stop and remove containers
make clean
```

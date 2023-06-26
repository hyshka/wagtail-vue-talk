# wagtail-vue-talk
How to vue wagtail in a better light


## Development with Docker

The Django server will run on port `8000`, and the Node.js server compiling the Vue.js app will run on port `8080`.

To access the Wagtail admin go to http://localhost:8000/admin/, login is `demo` / `demo123`.

The Vue.js app is expecting the Wagtail API to be avaialable at `localhost:8000/api/v2/`.

```
# build image and start containers
make up

# enter backend (python) container
make enter

# start django server (inside container)
django-admin.py runserver 0.0.0.0:8000

# enter frontend (node.js) container
make enter_fe

# start node server (inside container)
npm run serve

# stop and remove containers
make clean
```

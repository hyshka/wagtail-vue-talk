# Development
```
# install dependencies
npm install

# start local dev server
npm run serve
```

## Docker
```
# build image and start container
make up

# enter container
make enter

# start local dev server (inside container)
npm run serve

# stop and remove container
make clean
```

## Scaffolding with `vue-cli`
```
# Install vue-cli
npm install -g @vue/cli

# Create new project in folder "vue"
vue create vue

# Options:
# manually select features: Babel, Router, Linter / Formatter
# user history mode for router (yes)
# eslint + prettier
# disable lint on save, enable lint + fix on commit
# in dedicated config files
# save as a preset (no)

# Move into project folder
cd vue

# Start development server
npm run serve
```

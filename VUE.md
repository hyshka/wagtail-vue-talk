# Overview
- Vue.js intro
- Project scaffolding using vue-cli https://cli.vuejs.org/
- Routing and API calls for Wagtail
- Rendering Wagtail Streamfields as Vue.js components
- Server-side rendering or prerendering

## Scaffolding with `vue-cli`
```
# install vue-cli
npm install -g @vue/cli

# create new project in folder "vue"
vue create vue

# options:
# manually select features: Babel, Router, Vuex, Linter / Formatter
# user history mode for router (yes)
# eslint + prettier
# disable lint on save, enable lint + fix on commit
# in dedicated config files
# save as a preset (no)

# move into project folder
cd vue

# start local dev server
npm run serve
```

## Docker
```
# move into project folder
cd vue

# build image and start container
make up

# enter container
make enter

# stop and remove container
make clean
```

## Routing
### Flow
1. Page loads, Vue is initialized
2. Vue-router `beforeEach` navigation guard is triggered
4. Make request to Wagtail API's "find" using page path in URL
5. If Wagtail returns `302/200` response continue and mount appropriate Vue component and pass returned response (ie. page data)
6. If Wagtail returns `404` abort and mount NotFound component

### Wagtail API (http://docs.wagtail.io/en/v2.3/advanced_topics/api/v2/usage.html)
- Pages /api/v2/pages/
  - pagination: /api/v2/pages/?offset=20&limit=20
  - ordering: /api/v2/pages/?order=title
  - filtering: /api/v2/pages/?slug=about
  - specific fields: /api/v2/pages/<pk>/?fields=_,body,feed_image
  - find page by path: /api/v2/pages/find/?html_path=<path> 
- Images /api/v2/images/
- Documents /api/v2/documents/

## Streamfields
For each page we will get one big JSON object back from the Wagtail API with all of the content. We will use a Vue component to handle all of the different streamfields nested in the page content field and create a Vue component for each streamfield type.

For more control over the layout we could create a separate Vue component for each page type so that the rendering pipline might look like this:

1. In vue-router `reponse.meta.type` returns `pages.HomePage` so render component with matching name.
```
router.beforeEach((to, from, next) => {
  get(`/api/v2/pages/find/?html_path=${to.fullPath}`)
  .then(response => {
    // catch 302/200 response, render matching Vue component
    // TODO: test passing response as param
    next({ name: response.meta.type, params: { page: response }})
  }).catch(error => {
    // catch 404 response, page doesn't exist
    next({ name: "404" })
  })
})
```

2. For each object in `response.content` use `object.type` to render Vue component dynamically (https://vuejs.org/v2/guide/components.html#Dynamic-Components). This allows us to render different Vue components based off of which content streamfields were added to the page.

```
<component 
  v-for="object in response.content"
  v-bind:key="object.id"
  v-bind:is="object.type"></component>
```

## SSR/Prerendering
TODO
- https://ssr.vuejs.org/
- https://nuxtjs.org/
- https://github.com/chrisvfritz/prerender-spa-plugin

## Noteworthy packages
- vue.js https://vuejs.org
- vue-cli https://cli.vuejs.org/
- vue-router https://router.vuejs.org/
- vuex https://vuex.vuejs.org/
- vue-meta https://github.com/declandewet/vue-meta
- axios https://github.com/axios/axios

## Misc
- setup static host for staging
- page preview?
- admin on subdomain?
- do we even need vuex?
- try yarn?

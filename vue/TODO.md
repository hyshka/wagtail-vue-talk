# NOTES

## SSR/Prerendering
TODO
- https://ssr.vuejs.org/
- https://nuxtjs.org/
- https://github.com/chrisvfritz/prerender-spa-plugin

## Noteworthy packages
- vue.js https://vuejs.org
- vue-cli https://cli.vuejs.org/
- vue-router https://router.vuejs.org/
- vue-meta https://github.com/declandewet/vue-meta
- axios https://github.com/axios/axios

## Meta data
TODO: document
- all code is in WagtailPageHandler

## Async components for page views
TODO: document
- all code is in WagtailPageHandler
- loads vue components for page template as-needed
- integreated into webpack so they get split into separate bundles

## Page transition
TODO: document
- all code is in WagtailPageHandler
- using vue.js transition
- page views need to be keyed (to route path) and positioned absolute

## Lazy load images
TODO: document
- code in main.js and WagtailImage.vue
- using vue-lazyload (https://github.com/hilongjw/vue-lazyload)

## Misc
- setup static host for staging
- admin on subdomain
- page preview
- try yarn

## Gotchas
- Had to register streamfield component globally
- Can't assign a component dynamically from within vue-router
- Had to manually remove domain + port from URLs from the API to make then a relative path we could use for the router (Improve: move this into the router logic)

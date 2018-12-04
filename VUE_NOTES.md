# Wagtail + Vue.js Notes

## Intro
- Goals
  - Lay some foundation for using Wagtail as a headless CMS
  - Learn more about the inner workings of Wagtail and Vue.js
- Vue is a javascript framework commonly used for building user interfaces and single page applications.

## Routing
- We probably don't even need vue-router, or maybe there's a more flexible router that would allow us to dynamically render a component right inside the router

## Rendering Wagtail page content
- Explain how we map a Wagtail Streamfield to a Vue component

## Simple page navigation
- Explain how to build a custom query to the Wagtail API
- Page filtering and selectively including fields (underscore = start with clean slate)
  /api/v2/pages/?show_in_menus=true&fields=_,html_url,title


## Flavor
- I'm not stopping here
- How can we improve this
- Library agnostic, should be able to reproduce results in any framework (React, etc.)

## Gotchas
- Had to register streamfield component globally
- Can't assign a component dynamically from within vue-router
- Had to manually remove domain + port from URLs from the API to make then a relative path we could use for the router (Improve: move this into the router logic)

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

## Wagtail Images, Documents, and Streamfields
- Here, we have access to all of the fields and content that has been entered for this page
- Through the Wagtail API sometimes Images, Documents, and even Pages are returned with only an ID, for this I have created a few helper components that utilize the particular API endpoint to grab the data of each Image, Document, or Page with just it's ID. We are going to be using these all over the place so it's nice to have it abstracted out a bit. (Improve: add support for background images or lazy loaded images)
- We also have a special component to handle the Wagtail Streamfields. (TODO: explain what streamfields are) Basically for each block in the streamfield content we render this component once. Inside we are using Vue's dynamic components again to in turn load the vue component matching the block type in Wagtail. This provides us with a mechanism to create a fully modular Vue component for each type of streamfield block in Wagtail. Our template, styles, and javascript are now in one file for each streamfield, this will make them pretty portable between projects.
  - TODO: explain how component naming works
- In some streamfields we even render the streamfield component _again_. That's right, in Wagtail it's possible to nest the `StreamBlock` and we've found this useful particularily for creating customized layouts for richtext content. In order to nest the same component in Vue like this we need to register it as a global component in Vue. (TODO: expand on this)

TODO: refactor this
For each page we will get one big JSON object back from the Wagtail API with all of the content. We will use a Vue component to handle all of the different streamfields nested in the page content field and create a Vue component for each streamfield type.

For more control over the layout we could create a separate Vue component for each page type so that the rendering pipline might look like this:

2. For each object in `response.content` use `object.type` to render Vue component dynamically (https://vuejs.org/v2/guide/components.html#Dynamic-Components). This allows us to render different Vue components based off of which content streamfields were added to the page.

## Navigation
- In our `SiteHeader` component we fetch all the pages in Wagtail that have been marked as `show_in_menus`. This gives us something to build a simple menu with. (Improve: drop down menus, nested menu structure)
- specific fields: /api/v2/pages/<pk>/?fields=_,body,feed_image

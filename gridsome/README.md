# Wagtail frontend for Gridsome

To run the frontend, do `yarn` or `npm install`, then:

```
gridsome develop
```

## Guide

Add your Wagtail URL and security headers to the plugin options.

Details:
https://github.com/gridsome/gridsome/tree/master/packages/source-graphql

```js
// gridsome.config.js
module.exports = {
  plugins: [
    {
      use: '@gridsome/source-graphql',
      options: {
        url: 'https://example.com/api',
        fieldName: 'puppies',
        typeName: 'puppyTypes',

        headers: {
          Authorization: `Bearer ${process.env.AUTH_TOKEN}`,
        },
      },
    },
  ],
}
```

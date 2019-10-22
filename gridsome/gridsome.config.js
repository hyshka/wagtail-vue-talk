module.exports = {
  templates: {
    // Add templates for content types here.
    // Read more: https://gridsome.org/docs/templates/
  },
  plugins: [
    {
      use: '@gridsome/source-graphql',
      options: {
        url: 'http://backend:8000/graphql',

        fieldName: 'wagtail',
        // typeName: 'puppyTypes',

        // headers: {
        //   Authorization: `Bearer ${process.env.AUTH_TOKEN}`,
        // },
      },
    },
  ]
}

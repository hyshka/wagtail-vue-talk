<template>
  <Layout>
    <g-image alt="Example image" src="~/favicon.png" width="135" />
    <u>Hello, GraphQL!</u>
    <div v-for="page in $page.wagtail.pages" :key="page.id">
     <h2>{{ page.title }}</h2>
   </div>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Pariatur excepturi labore tempore expedita, et iste tenetur suscipit explicabo! Dolores, aperiam non officia eos quod asperiores</p>
  </Layout>
</template>

<script>
export default {}
</script>

<page-query>
query Wagtail {
  wagtail: wagtail {
    pages {
      id
      slug
      title
    }
  }
}
</page-query>

<!--
{ wagtail { pages {
	id
  slug
  title
  url
}}}
-->

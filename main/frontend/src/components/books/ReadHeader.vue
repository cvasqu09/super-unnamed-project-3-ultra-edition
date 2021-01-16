<template>
  <section class="is-flex">
    <div class="is-flex-grow-1">
      <h1 class="subtitle is-1">
        {{
          Number(totalPages).toLocaleString()
        }} Total Pages
      </h1>
    </div>
    <div class="is-flex-grow-1">
      <h1 class="subtitle is-1">
        {{ numberOfReviews }} Reviews Left
      </h1>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ReadHeader.vue',
  props: ['totalPages', 'numberOfReviews'],
};
</script>

<style scoped>

</style>

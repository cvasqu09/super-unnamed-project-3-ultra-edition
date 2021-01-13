<template>
  <div>
    <h1>Books here</h1>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'BookPage',
  data() {
    return {
      books: [],
    };
  },
  mounted() {
    axios.get('books/').then((res) => {
      this.books = res.data;
    });
  },
};
</script>

<style scoped>

</style>

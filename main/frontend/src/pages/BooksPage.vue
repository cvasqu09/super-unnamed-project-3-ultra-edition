<template>
  <div class="tile is-ancestor is-flex-wrap-wrap is-justify-content-space-between">
    <div class="tile is-4 px-3" v-for="book in books" :key="book.id">
      <book-card v-bind=book></book-card>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import BookCard from '@/components/books/BookCard.vue';

export default {
  name: 'BookPage',
  components: { BookCard },
  data() {
    return {
      books: [],
    };
  },
  mounted() {
    axios.get('books/', {
      params: {
        filter: 'to-read',
      },
    })
      .then((res) => {
        this.books = res.data;
      });
  },
};
</script>

<style scoped>

</style>

<template>
  <section>
    <div class="is-flex is-justify-content-flex-end px-4 py-4">
      <b-field label="Shelf">
        <b-select
          placeholder="Select a status"
          @input="updateBooks"
          :value="shelves[0].value">
          <option
            v-for="shelf in shelves"
            :value="shelf.value"
            :key="shelf.name">
            {{ shelf.name }}
          </option>
        </b-select>
      </b-field>
    </div>
    <div class="tile is-ancestor is-flex-wrap-wrap">
      <div class="tile is-4 px-3" v-for="book in books" :key="book.id">
        <book-card v-bind=book></book-card>
      </div>
    </div>
  </section>
</template>

<script>
import axios from 'axios';
import BookCard from '@/components/books/BookCard.vue';
import { shelfValues, Shelves } from '@/constants/book';

export default {
  name: 'BookPage',
  components: { BookCard },
  data() {
    return {
      books: [],
      shelves: [
        {
          name: Shelves.TO_READ,
          value: shelfValues[Shelves.TO_READ],
        },
        {
          name: Shelves.READ,
          value: shelfValues[Shelves.READ],
        },
        {
          name: Shelves.READING,
          value: shelfValues[Shelves.READING],
        },
      ],
    };
  },
  methods: {
    updateBooks(filter = shelfValues[Shelves.READ]) {
      axios.get('books/', {
        params: {
          filter,
        },
      })
        .then((res) => {
          this.books = res.data.map((book) => ({
            id: book.id,
            title: book.title,
            author: book.author,
            numberOfPages: book.number_of_pages,
            originalPublication: book.original_publication,
            yearPublished: book.year_published,
            isbn13: book.isbn_13,
          }));
        });
    },
  },
  mounted() {
    this.updateBooks(shelfValues[Shelves.TO_READ]);
  },
};
</script>

<style scoped>

</style>

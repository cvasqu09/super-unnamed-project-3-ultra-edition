<template>
  <div>
    <template v-if="selectedShelf === shelfValues[shelves.TO_READ]">
      <to-read-header :read-pages="bookStats.readPages"
                      :total-pages="bookStats.totalPages"></to-read-header>
    </template>
    <template v-else-if="selectedShelf === shelfValues[shelves.READ]">
      <read-header :total-pages="bookStats.totalPages"
                   :number-of-reviews="bookStats.numberOfReviews"></read-header>
    </template>
    <section>
      <div class="is-flex is-justify-content-flex-end px-4 py-4">
        <b-field label="Shelf">
          <b-select
            placeholder="Select a status"
            @input="updateBooks"
            v-model="selectedShelf">
            <option
              v-for="shelf in shelfOptions"
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
  </div>
</template>

<script>
import axios from 'axios';
import BookCard from '@/components/books/BookCard.vue';
import { shelfValues, Shelves } from '@/constants/book';
import ToReadHeader from '@/components/books/ToReadHeader.vue';
import ReadHeader from '@/components/books/ReadHeader.vue';

export default {
  name: 'BookPage',
  components: {
    ReadHeader,
    ToReadHeader,
    BookCard,
  },
  data() {
    return {
      bookStats: {},
      books: [],
      selectedShelf: shelfValues[Shelves.TO_READ],
      shelfValues,
      shelves: Shelves,
      shelfOptions: [
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
      console.log('selected shelf', this.selectedShelf);
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

    getBookStats() {
      axios.get('stats/books/')
        .then((res) => {
          this.bookStats = res.data;
        });
    },
  },
  mounted() {
    this.updateBooks(shelfValues[Shelves.TO_READ]);
    this.getBookStats();
  },
};
</script>

<style scoped>

</style>

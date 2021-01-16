<template>
  <base-card :title="titleWithYear">
    <img slot="image" :src="imageSource" alt="book-cover"/>
    <p slot="content">{{ author }}</p>
  </base-card>
</template>

<script>
import BaseCard from '@/components/ui/BaseCard.vue';

export default {
  name: 'BookCard',
  components: { BaseCard },
  data() {
    return {
      // eslint-disable-next-line global-require
      defaultImageSource: require('../../assets/images/default-book-cover.jpg'),
    };
  },
  props: {
    id: Number,
    title: String,
    author: String,
    originalPublication: Number,
    yearPublished: Number,
    numberOfPages: Number,
    isbn13: String,
  },
  computed: {
    titleWithYear() {
      const bookTitle = this.title;
      if (this.originalPublication) {
        return `${bookTitle} (${this.originalPublication})`;
      }

      if (this.yearPublished) {
        return `${bookTitle} (${this.yearPublished})`;
      }
      return bookTitle;
    },
    imageSource() {
      return this.isbn13 ? `http://covers.openlibrary.org/b/isbn/${this.isbn13}-L.jpg`
        : this.defaultImageSource;
    },
  },
};
</script>

<style scoped>
img {
  height: 500px
}
</style>

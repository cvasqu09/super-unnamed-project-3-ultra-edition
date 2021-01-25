<template>
  <section>
    <b-button class="is-primary" @click="navToAddJournal">
      <b-icon class="mr-1" pack="fas" icon="plus-square" size="is-small"></b-icon>
      Add New Journal
    </b-button>
    <section v-for="journal in journals" :key="journal.id">
      <h2>{{ journal.title }}</h2>
      <p>{{ journal.content }}</p>
    </section>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'JournalsListPage.vue',
  methods: {
    navToAddJournal() {
      this.$router.push({ name: 'add-journal' });
    },
  },
  data() {
    return {
      journals: [],
    };
  },
  mounted() {
    axios.get('/journals/')
      .then((res) => {
        this.journals = res.data;
      });
  },
};
</script>

<style scoped>

</style>

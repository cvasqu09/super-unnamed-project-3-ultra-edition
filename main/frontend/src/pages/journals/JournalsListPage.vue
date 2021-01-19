<template>
  <section>
    <h2>Journal List Page</h2>
    <b-button class="is-primary" @click="navToAddJournal">
      <b-icon pack="fas" icon="plus-square" size="is-small"></b-icon>
      Add
    </b-button>
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

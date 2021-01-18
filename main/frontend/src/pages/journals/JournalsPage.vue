<template>
  <section>
    <section class="is-flex">
      <b-button icon-left="plus-square"
                class="is-primary is-align-self-flex-end"
                @click="navToAddJournal">
        Add
      </b-button>
      <router-view></router-view>
    </section>

  </section>
</template>

<script>
import axios from 'axios';

export default {
  name: 'JournalsPage',
  data() {
    return {
      journals: [],
    };
  },
  methods: {
    navToAddJournal() {
      this.$router.push({ name: 'add-journal' });
    },
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

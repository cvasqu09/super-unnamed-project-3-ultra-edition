<template>
  <form class="p-2">
    <b-field label="Title" label-position="inside">
      <b-input v-model="title"></b-input>
    </b-field>

    <b-field label="Content" label-position="inside">
      <b-input v-model="content" maxlength="15000" type="textarea"></b-input>
    </b-field>

    <b-button class="is-primary fr" @click="saveJournal">
      Save
    </b-button>

  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'AddJournalForm',
  data() {
    return {
      title: '',
      content: '',
    };
  },
  methods: {
    saveJournal() {
      axios.post('/journals/', {
        title: this.title,
        content: this.content,
      });
    },
  },
};
</script>

<style scoped>
.fr {
  float: right;
}
</style>

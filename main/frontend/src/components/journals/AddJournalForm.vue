<template>
  <form>
    <b-field label="Title">
      <b-input v-model="title"></b-input>
    </b-field>

    <b-field label="content">
      <b-input maxlength="15000" type="textarea"></b-input>
    </b-field>
  </form>
</template>

<script>
export default {
  name: 'AddJournalForm',
  data() {
    return {
      title: '',
      content: '',
    };
  },
};
</script>

<style scoped>

</style>

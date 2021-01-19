<template>
  <section>
    <h2>Add Journal Here</h2>
    <add-journal-form></add-journal-form>
  </section>
</template>

<script>
import AddJournalForm from '@/components/journals/AddJournalForm.vue';

export default {
  name: 'AddJournalPage',
  components: { AddJournalForm },
};
</script>

<style scoped>

</style>

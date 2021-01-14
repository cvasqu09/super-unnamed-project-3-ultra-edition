<template>
  <base-card :title="title">
    <p slot="content">{{ author }}</p>
  </base-card>
</template>

<script>
import BaseCard from '@/components/ui/BaseCard.vue';

export default {
  name: 'BookCard',
  components: { BaseCard },
  props: {
    id: Number,
    title: String,
    author: String,
  },
};
</script>

<style scoped>

</style>

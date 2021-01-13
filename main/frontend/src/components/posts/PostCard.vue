<template>
  <div>
    <base-card :title="title">
      <div slot="content" id="card-content">
        <p>{{ description }}<p>
        <p id="date">{{ date }}</p>
      </div>
    </base-card>
  </div>
</template>

<script>
import BaseCard from '@/components/ui/BaseCard.vue';
import axios from 'axios';

export default {
  name: 'PostCard',
  components: { BaseCard },
  props: {
    title: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
  },

};
</script>

<style scoped lang="scss">
  #card-content {
    display: flex;
    flex-direction: column;

    #date {
      width: fit-content;
      justify-self: flex-start;
    }
  }
</style>

<template>
  <section class="is-flex is-align-items-center">
    <div class="is-flex-grow-1">
      <ProgressBar :progress="pageProgress"
                   description="Page Progress"></ProgressBar>
    </div>
    <div class="is-flex-grow-3">
      <h1 class="subtitle is-1">
        {{ totalPages.toLocaleString() }} Total Pages
      </h1>
    </div>
  </section>
</template>

<script>
import ProgressBar from '@/components/ui/ProgressBar.vue';

export default {
  name: 'ToReadHeader',
  components: { ProgressBar },
  props: {
    totalPages: {
      type: Number,
      default: 0,
    },
    readPages: {
      type: Number,
      default: 0,
    },
  },
  computed: {
    pageProgress() {
      if (this.readPages && this.totalPages && this.totalPages !== 0) {
        return ((this.readPages / this.totalPages) * 100).toFixed(2);
      }
      return 0;
    },
  },
};
</script>

<style scoped>

</style>

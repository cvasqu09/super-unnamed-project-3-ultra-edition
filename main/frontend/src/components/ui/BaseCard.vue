<template>
  <div class="card">
    <div class="card-header" v-if="title">
      <p class="card-header-title">
        {{ title }}
      </p>
    </div>
    <div class="card-content">
      <slot name="content"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseCard',
  props: {
    title: {
      type: String,
      required: false,
    },
  },
};
</script>

<style scoped>

</style>

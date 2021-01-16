<template>
  <div class="card" id="base-card-container">
    <div class="card-image">
      <slot name="image"></slot>
    </div>
    <div class="card-content">
      <p class="title">{{ title }}</p>
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
#base-card-container {
  width: 100%;
}
</style>

<template>
  <div class="home">
    <the-header></the-header>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import TheHeader from '@/components/ui/TheHeader.vue';

export default Vue.extend({
  name: 'Home',
  components: { TheHeader },
});
</script>

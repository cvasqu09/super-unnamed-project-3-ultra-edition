<template>
  <div class="home">
    <b-button tag="router-link" :to="{name: 'login'}">Login</b-button>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'Home',
  components: { },
});
</script>

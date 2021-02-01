<template>
  <form class="is-flex is-flex-direction-column form">
    <b-field label="Username" label-position="inside">
      <b-input v-model="username"></b-input>
    </b-field>
    <b-field label="Password" label-position="inside">
      <b-input type="password" v-model="password"></b-input>
    </b-field>
    <b-button class="is-primary mb-2" @click="login">Log In</b-button>
    <b-notification type="is-danger" v-if="error">
      Error logging in: {{error}}
    </b-notification>
  </form>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      error: null,
    };
  },
  methods: {
    login() {
      return this.$store.dispatch('login', { username: this.username, password: this.password });
    },
  },
};
</script>

<style scoped>
.form {
  margin: auto;
  width: 50%;
}
</style>

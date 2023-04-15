<template>
    <div class="login-form">
      <h2>Login</h2>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username">
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password">
        </div>
        <button type="submit">Login</button>
      </form>
    </div>
  </template>
  
  <script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm() {
      axios.post('http://127.0.0.1:8080/api/v1/auth/login', {
          username: this.username,
          password: this.password,
        })
        .then(response => {
          // Handle successful login response
          const user_id = response.data.id;
          localStorage.setItem("user_id",user_id)
          console.log(response.data)
          const token = response.data.access_token;
          localStorage.setItem("JWT",token)
        })
        .catch(error => {
          // Handle login error
          console.log(error.response.data)
        })
    }
  }
}
</script>

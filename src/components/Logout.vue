<template>
    <div class="logout-form">
      <h2>Logout</h2>
      <button @click="logoutUser">Logout</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  export default {
    name: 'Logout',
    methods: {
      logoutUser() {
        axios.post('http://127.0.0.1:8080/api/v1/auth/logout')
          .then(response => {
            console.log(response.data)
            // Clear the JWT token and user ID from local storage
            localStorage.removeItem('JWT')
            localStorage.removeItem('user_id')
            // Redirect the user to the login page
            this.$router.push('/login')
          })
          .catch(error => {
            console.log(error.response.data)
          })
      }
    }
  }
  </script>
  
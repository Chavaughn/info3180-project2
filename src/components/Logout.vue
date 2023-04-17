<template>
  <div class="content-box-border">
    <h2>Logout</h2>
    <p>Are you sure you would like to logout?</p>
    <div class="row col-md-12">
      <div class="col-md-6">
        <button class="form-control btn btn-danger" @click="logoutUser">Logout</button>
      </div>
      <div class="col-md-6">
        <button class="form-control" @click="goBack">Go Back</button>
      </div>
    </div>
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
          // Redirect the user to the home page
          window.location.href = "/"
        })
        .catch(error => {
          console.log(error.response.data)
        })
    },
    goBack() {
      this.$router.back()
    }
  }
}
</script>

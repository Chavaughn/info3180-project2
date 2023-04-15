<template>
    <div class="container">
      <h1>Registration Form</h1>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="form-group">
          <label for="firstname">First Name:</label>
          <input type="text" id="firstname" v-model="firstname" required>
        </div>
        <div class="form-group">
          <label for="lastname">Last Name:</label>
          <input type="text" id="lastname" v-model="lastname" required>
        </div>
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required>
        </div>
        <div class="form-group">
          <label for="location">Location:</label>
          <input type="text" id="location" v-model="location">
        </div>
        <div class="form-group">
          <label for="biography">Biography:</label>
          <textarea id="biography" v-model="biography"></textarea>
        </div>
        <div class="form-group">
          <label for="profile_photo">Profile Photo:</label>
          <input type="file" id="profile_photo" @change="handleFileUpload">
        </div>
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        firstname: '',
        lastname: '',
        email: '',
        location: '',
        biography: '',
        profile_photo: null,
        errors: []
      }
    },
    methods: {
      handleFileUpload(event) {
        this.profile_photo = event.target.files[0]
      },
      submitForm() {
        const formData = new FormData()
        formData.append('username', this.username)
        formData.append('password', this.password)
        formData.append('firstname', this.firstname)
        formData.append('lastname', this.lastname)
        formData.append('email', this.email)
        formData.append('location', this.location)
        formData.append('biography', this.biography)
        formData.append('profile_photo', this.profile_photo)
  
        axios.post('http://127.0.0.1:8080//api/v1/register', formData)
          .then(response => {
            this.$router.push('/login')
          })
          .catch(error => {
            if (error.response && error.response.status === 409) {
              this.errors.push(error.response.data.message)
            } else {
              this.errors.push('An error occurred. Please try again later.')
            }
          })
      }
    }
  }
  </script>
  
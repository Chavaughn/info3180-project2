<template>
    <div class="container">
      <h2>Create New Post</h2>
      <form @submit.prevent="submitForm" id="postForm">
        <div class="form-group">
          <label for="caption">Caption:</label>
          <input type="text" id="caption" v-model="caption">
        </div>
        <div class="form-group">
          <label for="photo">Photo:</label>
          <input type="file" id="photo" ref="photo" @change="onFileChange">
        </div>
        <button type="submit">Create Post</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'PostForm',
    data() {
      return {
        userId: localStorage.getItem('user_id'),   
      }
    },
  
    methods: {
      submitForm() {
        let form_data = new FormData();
        form_data.append('caption', this.caption);
        form_data.append('photo', this.photo);
        let token = localStorage.getItem('JWT');

        axios.post(`http://127.0.0.1:8080/api/v1/users/${this.userId}/posts`, form_data, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${token}`,
            'Access-Control-Allow-Origin': '*',
          }
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error.response.data);
        });
      },
      onFileChange(e) {
        this.photo = e.target.files[0]
      }
    }
  }
  </script>
  
<template>
  <h2>New Post</h2>
  <div class="create-post-container">
    <!--<div v-if="errorMessage">{{ errorMessage }}</div>-->
    <form @submit.prevent="submitForm" name="postForm" id="postForm">
      <div class="form-group">
        <label for="caption">Caption:</label>
        <textarea class="form-control" type="textarea" id="caption" name="caption"/>
      </div>
      <div class="form-group">
        <label for="photo">Photo:</label>
        <input class="form-control" type="file" id="photo" ref="photo" name="photo" @change="onFileChange">
      </div>
      <button class="form-control btn btn-success" type="submit">Create Post</button>
    </form>
  </div>
</template>
  
<script setup>
import axios from 'axios'
import { ref, onMounted, defineEmits } from "vue";
import { RouterLink } from "vue-router";

const emit = defineEmits(['notification', 'type']);


const token = localStorage.getItem('JWT');
const userId = localStorage.getItem('user_id');
const errorMessage = ref(null);

function submitForm() {
  let postForm = document.getElementById("postForm");
  let formData = new FormData(postForm);

  axios.post(`http://127.0.0.1:8080/api/v1/users/${userId}/posts`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
      'Authorization': `Bearer ${token}`,
      'Access-Control-Allow-Origin': '*',
    }
  })
    .then(response => {
      console.log(response.data);
      emit('notification', response.data.message);
      emit('type', "success");
    })
    .catch(error => {
      errorMessage.value = error.response.data.errors;
      emit('notification', errorMessage.value);
      emit('type', "danger");
      window.location.href = "#";
    });
}
function onFileChange(e) {
  this.photo = e.target.files[0]
}

</script>
  
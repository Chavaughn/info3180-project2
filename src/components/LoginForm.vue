<template>
  <div class="login-form">
    <form name="LoginForm" id="LoginForm" @submit.prevent="submitForm">
      <div class="form-group">
        <div class="col-md-12">
          <label for="username">Username:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="text" name="username" id="username" autocomplete="current-username" placeholder="Enter Username" />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="password">Password:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="password" name="password" id="password" autocomplete="current-password"
            placeholder="Enter Password" />
        </div>
      </div>
      <div class="pt-5 col-md-12">
        <button class="form-control btn btn-success" type="submit">Login</button>
      </div>
    </form>
  </div>
</template>
  
<script setup>
import axios from "axios";
import { ref } from "vue";

const errorMessage = ref(null);

let username = ref("");
let password = ref("");


function submitForm() {
  let loginForm = document.getElementById("LoginForm");
  let formData = new FormData(loginForm);
  username.value = formData.get("username");
  password.value = formData.get("password");
  axios.post("http://localhost:8080/api/v1/auth/login", {
    username: username.value,
    password: password.value,
  })
    .then((response) => {
      // Handle successful login response
      const user_id = response.data.id;
      localStorage.setItem("user_id", user_id);
      console.log(response.data);
      const token = response.data.access_token;
      localStorage.setItem("JWT", token);
      window.location.href = `/explore`;
    })
    .catch((error) => {
      // Handle login error
      console.log(error.response.data);
      errorMessage.value = error.response.data.message;
    });
}
</script>
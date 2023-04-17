<template>
  <div class="login-form">
    <h1>Registration Form</h1>
    <form id="RegisterForm" @submit.prevent="submitForm">
      <div class="form-group">
        <div class="col-md-12">
          <label for="username">Username:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="text" name="username" id="username" required autocomplete="username" />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="password">Password:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="password" name="password" id="password" required  />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="firstname">First Name:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="text" name="firstname" id="firstname" required autocomplete="given-name" />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="lastname">Last Name:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="text" name="lastname" id="lastname" required autocomplete="family-name" />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="email">Email:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="email" name="email" id="email" required autocomplete="email" />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="location">Location:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="text" name="location" id="location" autocomplete="address-line1" />
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="biography">Biography:</label>
        </div>
        <div class="col-md-12">
          <textarea class="form-control" id="biography" name="biography"></textarea>
        </div>
      </div>
      <div class="form-group">
        <div class="col-md-12">
          <label for="profile_photo">Profile Photo:</label>
        </div>
        <div class="col-md-12">
          <input class="form-control" type="file" name="profile_photo" id="profile_photo" />
        </div>
      </div>
      <div class="pt-5 col-md-12">
        <button class="form-control btn btn-success" type="submit">Register</button>
      </div>
    </form>

  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

const errorMessage = ref(null);

function submitForm() {
  let registerForm = document.getElementById("RegisterForm");
  let formData = new FormData(registerForm);
  console.log(formData)
  fetch("http://localhost:8080//api/v1/register", {
    method: "POST",
    body: formData,
  })
    .then(function (response) {
      return response.json;
    })
    .then(function (data) {
      window.location.href = "/login";
    })
    .catch(function (error) {
      console.log(error);
      errorMessage.value = error.response.data.message;
    });
}
</script>

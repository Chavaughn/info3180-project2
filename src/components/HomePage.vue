<template>
    <div class="landing-inner">
      <h1 class="header-text"><i class="fa fa-camera"></i> BuddyGram</h1>
      <hr>
      <p>Your world at your fingertips! Share your favourite moments with friends family and the world!</p>
      <div class="landing-buttons">
        <button class="btn btn-success" @click="register">Register</button>
        <button class="btn btn-primary" @click="signIn">Sign In</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from "axios";
  import { ref } from "vue";
  
  function register() {
    window.location.href = '/register'
}

function signIn() {
      window.location.href = '/login'
  }
  </script>
  
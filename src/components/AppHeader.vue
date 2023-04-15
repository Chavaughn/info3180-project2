<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="/"><i class="fa fa-camera"></i> BuddyGram</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink  to="/" class="nav-link active">Home</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link" to="/about">About</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link" to="/register">Register</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link" to="/login">Login</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link" to="/logout">Logout</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link" to="/explore">Explore</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" :to="`/users/${user_id}`">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink  class="nav-link" to="/posts/new">Create Post</RouterLink >
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
  import { RouterLink } from "vue-router";
  let user_id = localStorage.getItem('user_id')
</script>

<style>
/* Add any component specific styles here */
</style>
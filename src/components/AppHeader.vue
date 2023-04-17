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
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <RouterLink v-if="!isAuthenticated" class="nav-link" to="/register">Register</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink v-if="!isAuthenticated" class="nav-link" to="/login">Login</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink v-if="isAuthenticated" class="nav-link" to="/explore">Explore</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink v-if="isAuthenticated" class="nav-link" :to="`/users/${userId}`">My Profile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink v-if="isAuthenticated" class="nav-link" to="/posts/new">Create Post</RouterLink >
            </li>
            <li class="nav-item">
              <RouterLink v-if="isAuthenticated" class="nav-link" to="/logout">Logout</RouterLink >
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      return localStorage.getItem('JWT') !== null;
    },
    userId() {
      return localStorage.getItem('user_id');
    }
  }
};
</script>

<style>
  .navbar-nav {
    float: right;
    padding-right: 0.5rem;
  }
</style>

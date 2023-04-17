<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import loginImage from './assets/login-img.jpg'

</script>

<template>
  <AppHeader />

  <main>
    <div class="main-content-view">
      <RouterView />
    </div>
    <AppFooter />
  </main>
  
</template>

<style>
body {
  padding-top: 75px;
}
</style>
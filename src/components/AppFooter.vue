<template>
      <div class="footer">
          <div class="container">
              <p>Copyright &copy {{ year }} Web Dev Project 2</p>
          </div>
      </div>
</template>

<script setup>
import { ref } from "vue";

const year = (new Date).getFullYear();
</script>

<style>
/* Add any component specific styles here */
</style>
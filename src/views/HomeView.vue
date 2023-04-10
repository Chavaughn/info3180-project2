<script setup>
import { ref } from "vue";
import { Tooltip, Popover, Button } from "bootstrap";

let message = ref("Hello World! This is a VueJS and Flask Starter Template.");

new Tooltip(document.body, {
  selector: "[data-bs-toggle='tooltip']",
});
</script>

<template>
  <div class="container">
    <div class="text-center">
      <span
      data-bs-toggle="tooltip"
      data-bs-placement="bottom"
      data-bs-html="true"
      title="<u>Kill self now Yohance</u>"
      >
      <img
        alt="Vue logo"
        class="logo"
        src="@/assets/logo.svg"
        width="125"
        height="125"
      />
    </span>
    <h1>{{ message }}</h1>
    </div>
  </div>
</template>

<style>
/* Add any component specific styles here */
</style>

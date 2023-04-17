<script setup>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import AppFooter from "@/components/AppFooter.vue";
import loginImage from './assets/login-img.jpg'
import Notifications from './components/Notifications.vue';
import { ref, defineEmits } from "vue";

// const emit = defineEmits(['notification']);


const appMessage = ref(null);
const messageType = ref(null);

function clearError() {
  appMessage.value = null;
  messageType.value = null;
}
function handleMessage(msg) {
  appMessage.value = Array.isArray(msg) ? msg : [msg];
}
function handleMessageType(type) {
  messageType.value = type;
}
</script>

<template>
  <AppHeader />

  <main>
      <Notifications v-if="appMessage" :type="messageType" :message="appMessage" @hide="clearError"/>
    <div class="main-content-view">
        <RouterView @notification="handleMessage" @type="handleMessageType"/>
    </div>
    <AppFooter />
  </main>
  
</template>

<style>
body {
  padding-top: 75px;
}
.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>

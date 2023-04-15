<script>
import { ref } from "vue";
import  HomePage  from "@/components/HomePage.vue";
import loginImage from '@/assets/login-img.jpg'

export default {
    name: "HomeView",
    components:{
        HomePage,
    },
  setup() {
    const imageSrc = ref(loginImage);
    return { imageSrc };
  },
};
</script>

<template >
    <img class="login-img" :src="imageSrc" alt="A pretty image">
    <div class="content-box-border landing">
        <HomePage />
    </div>
</template>

<style>

</style>
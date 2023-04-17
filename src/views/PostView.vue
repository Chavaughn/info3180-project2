<script>
import { ref } from "vue";
import PostForm from "@/components/PostForm.vue";

export default {
  name: "PostView",
  components: {
    PostForm,
  },
};
</script>

<template>
    <div class="post-page">
    <div class="page-title">
    </div>
    <div class="create-post-page">
        <PostForm/>
    </div>
  </div>
</template>

<style></style>

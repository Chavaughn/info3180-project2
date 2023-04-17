<script>
import { ref } from "vue";
import PostForm from "@/components/PostForm.vue";

export default {
  name: "PostView",
  components: {
    PostForm,
  },
  methods: {
    handleError(event){
        this.$emit('notification', event)
    },
    handleMessageType(event){
        this.$emit('type', event)
    }
  }
};
</script>

<template>
    <div class="post-page">
    <div class="page-title">
    </div>
    <div class="create-post-page">
        <PostForm @notification = "handleError" @type = "handleMessageType" />
    </div>
  </div>
</template>

<style></style>

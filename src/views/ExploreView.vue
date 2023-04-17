<script>
import { ref } from "vue";
import ExplorePage from "@/components/ExplorePage.vue";

export default {
  name: "ExploreView",
  components: {
    ExplorePage,
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
    <div class="explore-page">
    <div class="page-title">
        <h2>Explore Posts</h2>
    </div>
    <div class="explore-page">
        <ExplorePage @notification = "handleError" @type = "handleMessageType" />
    </div>
  </div>
</template>

<style></style>

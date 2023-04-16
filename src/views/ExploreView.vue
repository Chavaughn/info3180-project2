<script>
import { ref } from "vue";
import ExplorePage from "@/components/ExplorePage.vue";

export default {
  name: "ExploreView",
  components: {
    ExplorePage,
  },
};
</script>

<template>
    <div class="explore-page">
    <div class="page-title">
        <h2>Explore Posts</h2>
    </div>
    <div class="explore-page">
        <ExplorePage />
    </div>
  </div>
</template>

<style></style>

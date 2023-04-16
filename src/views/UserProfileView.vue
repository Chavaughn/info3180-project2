<script>
import { ref } from "vue";
import UserProfilePage from "@/components/UserProfilePage.vue";

export default {
  name: "UserProfileView",
  components: {
    UserProfilePage,
  },
  props: {
    id: {
      type: String,
      required: true,
    }
}
};
</script>

<template>
    <div class="profile-page">
    <div class="page-title">
        <h2>Explore Posts</h2>
    </div>
    <div class="user-profile-page">
        <UserProfilePage :id= id />
    </div>
  </div>
</template>

<style></style>

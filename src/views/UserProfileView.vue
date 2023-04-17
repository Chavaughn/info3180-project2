<script setup>
import { ref, defineEmits } from "vue";

const emits = defineEmits(['notification' , 'type']);
</script>

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
    },
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
  <div class="profile-page">
    <div class="page-title"></div>
    <div class="user-profile-page">
      <UserProfilePage :id="id" @notification = "handleError" @type = "handleMessageType" />
    </div>
  </div>
</template>

<style></style>

<template>
  <div class="page">
    <div class="user-profile">
      <div class="user-info">
        <div class="photo-section">
          <img class="profile-photo" :src="user.profile_photo" alt="profile picture" />
        </div>
        <div class="about-section">
          <h2 class="name">{{ user.first_name }} {{ user.last_name }}
            <hr>
          </h2>
          <p class="location">{{ user.location }}</p>
          <p class="joined">Member since {{ user.joined_on }}</p>
          <p class="bio">{{ user.biography }}</p>
        </div>
        <div class="number-section">
          <div class="posts-followers">
            <div class="posts">
              <p class="numbers">{{ numPosts() }}</p>
              <p>Posts</p>
            </div>
            <div class="followers">
              <p class="numbers">{{ numFollowers() }}</p>
              <p>Followers</p>
            </div>
          </div>
          <div class="follow-button-container">
            <button class="btn follow-button" v-if="!isFollowing" @click="followUser()">Follow</button>
            <button class="btn follow-button following" v-if="isFollowing" @click="followUser()">Following</button>
          </div>

        </div>
      </div>
      <div class="user-posts">
        <div v-for="post in userPosts" :key="post.id" class="post">
          <div class="post-wrapper">
            <img class="post-image" :src="post.photo_url" alt="post photo" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted, defineEmits } from "vue";
import { RouterLink } from "vue-router";

const user = ref({});
const userPosts = ref([]);
const followers = ref([]);
const isFollowing = ref(false);
const errorMessage = ref(null);

const props = defineProps({
  id: {
    type: String,
    required: true,
  }

});

const emit = defineEmits(['notification', 'type']);


onMounted(() => {
  let token = localStorage.getItem("JWT");
  // Get user's posts
  axios
    .get(`http://localhost:8080/api/v1/users/${props.id}/posts`, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Access-Control-Allow-Origin": "*",
      },
    })
    .then((response) => {
      user.value = response.data.user;
      userPosts.value = response.data.posts;
      followers.value = response.data.follows;
      if (followers.value.some((follower) => follower.follower_id = props.id)) {
        isFollowing.value = true;
      }
      

    })
    .catch((error) => {
      errorMessage.value = error.response.data.msg;
      console.log('Error:', errorMessage.value);
      emit('notification', errorMessage.value);
      emit('type', "danger");
      window.location.href = "#";
    })
});

function numPosts() {
  return userPosts.value.length;
}
function numFollowers() {
  return followers.value.length;
}
function followUser() {
  let token = localStorage.getItem("JWT");

  axios
    .post(
      `http://localhost:8080/api/v1/users/${props.id}/follow`,
      {},
      {
        headers: {
          Authorization: `Bearer ${token}`,
          "Access-Control-Allow-Origin": "*",
        },
      }
    )
    .then((response) => {
      isFollowing.value = true;
      console.log(response.data);
      followers.value.push(response.data.follower);
      emit('notification', response.data.message);
      emit('type', "success");
    })
    .catch((error) => {
      errorMessage.value = error.response.data.message;
      console.log('Error:', errorMessage.value);
      emit('notification', errorMessage.value);
      emit('type', "danger");
      window.location.href = "#";
    });
}
</script>
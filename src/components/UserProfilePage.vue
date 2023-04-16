<template>
  <div class="page">
    <div class="user-profile">
      <div class="user-info">
        <div class="photo-section">
          <img class="profile-photo" :src="user.profile_photo" alt="profile picture">
        </div>
        <div class="about-section">
          <h2 class="name">{{ user.firstname }} {{ user.lastname }}</h2>
          <p class="location">Location: {{ user.location }}</p>
          <p class="joined">Member since: {{ user.joined_on }}</p>
          <p class="bio">{{ user.biography }}</p>
        </div>
        <div class="number-section">
          <div class="posts-followers">
            <div class="posts">
              <p>Posts: {{ numPosts() }}</p>
            </div>
            <div class="followers">
              <p>Followers: {{ numFollowers() }}</p>
            </div>
          </div>
          <div class="follow-button"></div>
          <button v-if="!isFollowing" @click="followUser()">Follow</button>
        </div>
      </div>

      <div class="user-posts">
        <div v-for="post in userPosts" :key="post.id" class="post">
          <img class="post-image" :src="post.photo_url" alt="post photo">
        </div>
      </div>
    </div>
  </div>
</template>
  
  
<script setup>
import axios from 'axios'
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";

const user = ref({});
const userPosts = ref([]);
const followers = ref([]);
const isFollowing = ref(false);

const props = defineProps({
  id: {
    type: String,
    required: true,
  },
});

onMounted(() => {
  let token = localStorage.getItem('JWT');
  // Get user's posts
  axios.get(`http://localhost:8080/api/v1/users/${props.id}/posts`, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Access-Control-Allow-Origin': '*',
    }
  })
    .then(response => {
      console.log(response)
      user.value = response.data.user;
      userPosts.value = response.data.posts
      followers.value = response.data.follows
    })
    .catch(error => {
      console.log(error.response.data)
    })
});

function numPosts() {
  return userPosts.value.length
};
function numFollowers() {
  return followers.value.length
};
function followUser() {
  let token = localStorage.getItem('JWT')

  axios.post(`http://localhost:8080/api/v1/users/${props.id}/follow`, {}, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Access-Control-Allow-Origin': '*',
    }
  })
    .then(response => {
      isFollowing.value = true
      console.log(response.data)
      followers.value.push(response.data.follower)
    })
    .catch(error => {
      console.log(error.response.data)
    })
}
</script>

<template>
  <div class="page">
    <div class="posts">
      <div v-for="post in posts" :key="post.id" class="post">
        <div class="post-creator">
          <img class="profile-photo" :src="post.user_photo" alt="creator photo">
          <h5>{{ post.username }}</h5>
        </div>
        <div class="post-body">
          <img :src="post.photo_url" alt="post photo">
          <p>{{ post.caption }}</p>
        </div>
        <div class="post-footer">
            <i class="like-button fa form-control btn" :class="{ 'fa-heart red': postLiked(post), 'fa-heart-o': !postLiked(post) }"
             v-on:click="likePost(post.id)">{{ post.num_likes }}</i>
             <p>{{ post.created_on }}</p>
        </div>
      </div>
    </div>
    <div class="add-post-button">
      <button class="btn" type="button"><router-link to="/posts/new"><i class="fa fa-plus-circle">New Post</i></router-link></button>
    </div>
  </div>
</template>

  
<script setup>
import axios from 'axios'
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";

const posts = ref([]);
const token = localStorage.getItem('JWT');

onMounted(() => {
  axios.get('http://127.0.0.1:8080/api/v1/posts', {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Access-Control-Allow-Origin': '*',
    }
  })
  .then(response => {
    posts.value = response.data;
    console.log(posts.value);
  })
  .catch(error => {
    console.log(error.response.data);
  });
});

function likePost(postId) {
  axios.post(`http://127.0.0.1:8080/api/v1/posts/${postId}/like`, null, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Access-Control-Allow-Origin': '*',
    }
  })
  .then(response => {
    console.log(response.data)
    // Update the post object in the posts array to reflect the new like
    let post = posts.value.find(p => p.id === postId);
    post.likes.push(response.data.like);
  })
  .catch(error => {
    console.log(error.response.data);
  });
}

function postLiked(post) {
  return post?.likes.some(like => like.user_id === post.user_id)
}
</script>

  
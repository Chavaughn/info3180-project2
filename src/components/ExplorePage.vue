<template>
  <div class="page">
    <div class="posts">
      <div v-for="post in posts" :key="post.id" class="post">
        <div class="post-creator">
          <img class="profile-photo" :src="post.user_photo" alt="creator photo">
          <h5 class="post-creater-user">
            <RouterLink :to="{ name: 'UserProfile', params: { id: post.user_id } }">{{ post.username }}</RouterLink>
          </h5>
        </div>
        <div class="post-body">
          <img :src="post.photo_url" alt="post photo">
          <p>{{ post.caption }}</p>
        </div>
        <div class="post-footer">
          <i v-if="postLiked(post)" class="like-button fa fa-heart red form-control btn"
            v-on:click="unlikePost(post.id)">{{ post.num_likes }}</i>
          <i v-else class="like-button fa fa-heart-o form-control btn" v-on:click="likePost(post.id)">{{ post.num_likes
          }}</i>
          <p>{{ post.created_on }}</p>
        </div>
      </div>
    </div>
    <div class="add-post-button-container">
      <button class="add-post-button btn btn-success form-control" type="button"><router-link :to =  "{name: 'NewPost'}"><i
            class="fa fa-plus-circle">&nbsp;&nbsp;New Post</i></router-link></button>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted } from "vue";
import { RouterLink } from "vue-router";
import { checkTokenExpiration } from './utils';

const posts = ref([]);
const errorMessage = ref(null);
const token = localStorage.getItem('JWT');
const user_id = localStorage.getItem('user_id');

onMounted(() => {
  checkTokenExpiration();

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
      errorMessage.value = error.response.data.message;
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
      let post = posts.value.find(p => p.id === postId);
      post.likes.push(response.data.like);
      post.num_likes = post.num_likes + 1;
    })
    .catch(error => {
      console.log(error.response);
      errorMessage.value = error.response.data.message;
    });
}

function unlikePost(postId) {
  axios.delete(`http://127.0.0.1:8080/api/v1/posts/${postId}/like`, {
    headers: {
      'Authorization': `Bearer ${token}`,
      'Access-Control-Allow-Origin': '*',
    }
  })
    .then(response => {
      let post = posts.value.find(p => p.id === postId);
      post.likes.splice(post.likes.indexOf(parseInt(user_id)), 1);
      post.num_likes = post.num_likes - 1;
    })
    .catch(error => {
      console.log(error.response);
      errorMessage.value = error.response.data.message;
    });
}

function postLiked(post) {
  return post?.likes.some(like => like === parseInt(user_id))
}
</script>

  
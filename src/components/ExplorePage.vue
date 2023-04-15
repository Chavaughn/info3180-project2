<template>
    <div class="container">
      <h2>Explore Posts</h2>
      <div v-for="post in posts" :key="post.id">
        <h3>{{ post.caption }}</h3>
        <img :src="post.photo_url" alt="post photo">
        <p>Created by {{ post.username}} on {{ post.created_on }}</p>
        <button v-on:click="likePost(post.id)">Like</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'ExplorePage',
    data() {
      return {
        posts: []
      }
    },
    created() {
      let token = localStorage.getItem('JWT');
      axios.get('http://127.0.0.1:8080/api/v1/posts', {
        headers: {
          'Authorization': `Bearer ${token}`,
          'Access-Control-Allow-Origin': '*',
        }
      })
        .then(response => {
          this.posts = response.data
        })
        .catch(error => {
          console.log(error.response.data)
        })
    },
    methods: {
      likePost(postId) {
        let token = localStorage.getItem('JWT');
        axios.post(`http://127.0.0.1:8080/api/v1/posts/${postId}/like`, null, {
          headers: {
            'Authorization': `Bearer ${token}`,
            'Access-Control-Allow-Origin': '*',
          }
        })
          .then(response => {
            console.log(response.data)
            // Update the post object in the posts array to reflect the new like
            let post = this.posts.find(p => p.id === postId)
            post.likes.push(response.data.like)
          })
          .catch(error => {
            console.log(error.response.data)
          })
      }
    }
  }
  </script>
  
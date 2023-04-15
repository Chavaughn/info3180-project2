<template>
    <div class="container">
      <div class="user-profile">
        <div class="user-info">
            <img :src="user.profile_photo" alt="profile picture">
            <div class="user-text">
                <h2>{{ user.firstname }} {{ user.lastname }}</h2>
                <p>Location: {{ user.location }}</p>
                <p>Member since: {{ user.joined_on }}</p>
                <p>{{ user.biography }}</p>
                <p>Posts: {{ numPosts }}</p>
                <p>Followers: {{ numFollowers }}</p>
                <button v-if="!isFollowing" @click="followUser">Follow</button>
            </div>
            </div>

        <div class="user-posts">
          <h2>User Posts</h2>
          <div v-for="post in userPosts" :key="post.id">
            <h3>{{ post.caption }}</h3>
            <img :src="post.photo_url" alt="post photo">
            <p>Created on {{ post.created_on }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  <script>
  import axios from 'axios'
  
  export default {
    name: 'UserProfilePage',
    props: ['id'],
    data() {
      return {
        user: {},
        userPosts: [],
        followers:[],
        isFollowing: false,
      }
    },
    computed: {
        numPosts() {
            return this.userPosts.length
        },
        numFollowers() {
            return this.followers.length
        }
    },
    created() {
        let token = localStorage.getItem('JWT');
  
      // Get user's posts
      axios.get(`http://127.0.0.1:8080/api/v1/users/${this.id}/posts`, {
        headers: {
            'Authorization': `Bearer ${token}`,
            'Access-Control-Allow-Origin': '*',
        }
        })
        .then(response => {
            this.user = response.data.user;
            this.userPosts = response.data.posts
            this.followers = response.data.follows
        })
        .catch(error => {
            console.log(error.response.data)
        })
    },
    methods: {
    followUser() {
      let token = localStorage.getItem('JWT')

      axios.post(`http://127.0.0.1:8080/api/v1/users/${this.id}/follow`, {},{
        headers: {
          'Authorization': `Bearer ${token}`,
          'Access-Control-Allow-Origin': '*',
        }
      })
        .then(response => {
          this.isFollowing = true
          console.log(response.data)
          this.followers.push(response.data.follower)
        })
        .catch(error => {
          console.log(error.response.data)
        })
    }}

  }
  </script>
  
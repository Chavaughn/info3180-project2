import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegistrationForm from '@/components/RegistrationForm.vue'
import LoginForm from '@/components/LoginForm.vue'
import Logout from '@/components/Logout.vue'
import PostForm from '@/components/PostForm.vue'
import ExplorePage from '@/components/ExplorePage.vue'
import UserProfilePage from '@/components/UserProfilePage.vue'

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes: [{
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/about',
            name: 'about',
            // route level code-splitting
            // this generates a separate chunk (About.[hash].js) for this route
            // which is lazy-loaded when the route is visited.
            component: () =>
                import ('../views/AboutView.vue'),
        },
        { path: '/register', component: RegistrationForm },
        { path: '/login', component: LoginForm },
        { path: '/logout', component: Logout },
        { path: '/explore', component: ExplorePage },
        { path: '/users/:id', component: UserProfilePage, props: true },
        { path: '/posts/new', component: PostForm }
    ]
})



  
  

export default router
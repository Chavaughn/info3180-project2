import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegistrationForm from "@/views/RegistrationView.vue";
import LoginForm from "@/views/LoginView.vue";
import Logout from "@/components/Logout.vue";
import PostForm from "@/views/PostView.vue";
import ExplorePage from "@/views/ExploreView.vue";
import UserProfilePage from "@/views/UserProfileView.vue";

const routes = [{
        path: "/",
        name: "home",
        component: HomeView,
    },
    {
        path: "/about",
        name: "about",
        component: () =>
            import ("../views/AboutView.vue"),
    },
    {
        path: "/register",
        name: "Register",
        component: RegistrationForm
    },
    {
        path: "/login",
        name: "Login",
        component: LoginForm
    },
    {
        path: "/logout",
        name: "Logout",
        component: Logout,
        meta: { requiresAuth: true }
    },
    {
        path: "/explore",
        name: "Explore",
        component: ExplorePage,
        meta: { requiresAuth: true }
    },
    {
        path: "/users/:id",
        name: "UserProfile",
        component: UserProfilePage,
        meta: { requiresAuth: true },
        props: true
    },
    {
        path: "/posts/new",
        name: "NewPost",
        meta: { requiresAuth: true },
        component: PostForm
    },
];

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL
    ),
    routes
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        const token = localStorage.getItem('JWT')
        if (!token) {
            next({ name: 'home' }) // Redirect to login page
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router;
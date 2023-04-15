import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegistrationForm from "@/views/RegistrationView.vue";
import LoginForm from "@/views/LoginView.vue";
import Logout from "@/components/Logout.vue";
import PostForm from "@/components/PostForm.vue";
import ExplorePage from "@/components/ExplorePage.vue";
import UserProfilePage from "@/components/UserProfilePage.vue";

const router = createRouter({
    history: createWebHistory(
        import.meta.env.BASE_URL),
    routes: [{
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
            component: RegistrationForm
        },
        {
            path: "/login",
            component: LoginForm
        },
        {
            path: "/logout",
            component: Logout
        },
        {
            path: "/explore",
            component: ExplorePage
        },
        {
            path: "/users/:id",
            component: UserProfilePage,
            props: true
        },
        {
            path: "/posts/new",
            component: PostForm
        },
    ],
});

export default router;
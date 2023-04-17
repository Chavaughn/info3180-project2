<script>
import { ref } from "vue";
import  LoginForm  from "@/components/LoginForm.vue";

export default {
    name: "LoginView",
    components:{
        LoginForm,
    }
};
</script>

<template >
    <div class="forms-view">
        <div class="form-header">
            <h2>Login</h2>
        </div>
        <div class="form-body content-box-border login">
            <LoginForm />
        </div>
    </div>
</template>

<style>

</style>
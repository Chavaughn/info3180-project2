<script setup>
import { ref, defineEmits } from "vue";

const emits = defineEmits(['notification' , 'type']);
</script>

<script>
import { ref } from "vue";
import  LoginForm  from "@/components/LoginForm.vue";

export default {
    name: "LoginView",
    components:{
        LoginForm,
    },
  methods: {
    handleError(event){
        this.$emit('notification', event)
    },
    handleMessageType(event){
        this.$emit('type', event)
    }
  }
};
</script>

<template >
    <div class="forms-view">
        <div class="form-header">
            <h2>Login</h2>
        </div>
        <div class="form-body content-box-border login">
            <LoginForm @notification = "handleError" @type = "handleMessageType" />
        </div>
    </div>
</template>

<style>

</style>
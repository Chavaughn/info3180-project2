<script>
import { ref } from "vue";
import  RegistrationForm  from "@/components/RegistrationForm.vue";

export default {
    name: "RegistrationView",
    components:{
        RegistrationForm,
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
            <h2>Register</h2>
        </div>
        <div class="form-body register content-box-border">
            <RegistrationForm @notification = "handleError" @type = "handleMessageType" />
        </div>
    </div>
</template>

<style>

</style>
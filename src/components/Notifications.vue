<template>
  <div class="notification-container fade-in" v-if="show">
    <div class="notification">
      <div id="noti-inner" :class="['notification', 'notification-' + type]">
        <ul>
        <li v-for="errorMsg in message" :key="errorMsg">{{ errorMsg }}</li>
      </ul>
      </div>
    </div>
    <button 
      type="button"
      class="delete btn-close"
      aria-label="Close"
      @click="hide"
    ></button>
  </div>
</template>

<script>
export default {
  name: "Notification",
  props: {
    type: String,
    message: Array,
    duration: {
      type: Number,
      default: 300000,
    },
    errorMessage: String,
  },
  data() {
    return {
      show: true,
    };
  },
  mounted() {
    setTimeout(() => {
      this.hide();
    }, this.duration);
  },
  methods: {
    hide() {
      this.show = false;
      this.$emit("hide");
    },
  },
};
</script>

<style>
.notification-container {
  position: sticky;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  top: 0;
}

.notification {
  position: relative;
  padding: 1rem;
  border-radius: 0.25rem;
  color: #fff;
}

.notification-success {
  background-color: #4caf50;
}

.notification-info {
  background-color: #2196f3;
}

.notification-warning {
  background-color: #ffc107;
}

.notification-danger {
  background: #ff1100be;
}

.delete {
  padding-left: 20px;
  position: relative;
}
.fade-in {
  animation: fadeIn 2s;
  opacity: 0.8;
}
@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 0.8;
  }
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}
</style>

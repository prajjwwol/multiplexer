<template>
  <div class="login-container">
    <div class="login-form">
      <label for="email">
        <input
          type="email"
          id="email"
          v-model="email"
          placeholder="Email"
          @focus="focusInput"
          @blur="blurInput"
        />
      </label>
      <label for="password">
        <input
          type="password"
          id="password"
          v-model="password"
          placeholder="Password"
          @focus="focusInput"
          @blur="blurInput"
        />
      </label>
      <button @click="login">Login</button>
      <p v-if="error" class="error-message">{{ error }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      password: "",
      focused: false,
      error: ""
    };
  },
  methods: {
    focusInput() {
      this.focused = true;
    },
    blurInput() {
      this.focused = false;
    },
    login() {
      // Replace with your actual authentication logic
      if (this.email === 'user@example.com' && this.password === 'password') {
        this.$router.push({ name: 'multiplexer-selection' });
      } else {
        this.error = "Incorrect username or password";
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(120deg, #a6c0fe 0%, #f68084 100%);
  background-size: 200% 200%;
  animation: gradient 15s ease infinite;
}

.login-form {
  background: rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 20px;
  width: 300px;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.2);
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

input:focus {
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}

button {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 5px;
  background-color: #f68084;
  color: white;
  cursor: pointer;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

button:hover {
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
}

@keyframes gradient {
  0% { background-position: 200% 0%; }
  50% { background-position: 100% 100%; }
  100% { background-position: 0% 200%; }
}
</style>

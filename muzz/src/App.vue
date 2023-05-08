<template>
  <div class="container">
    <h1>HIL Multiplexer</h1>
    <p v-if="currentUser">Logged in as {{ currentUser }}</p>
    <div v-if="!currentUser">
      <label for="username">Username:</label>
      <input type="text" id="username" v-model="loginUsername">
      <label for="password">Password:</label>
      <input type="password" id="password" v-model="loginPassword">
      <button @click="login">Log In</button>
      <p v-if="loginError">{{ loginError }}</p>
    </div>
    <ul v-if="currentUser">
      <li v-for="(device, index) in devices" :key="index">
        <div class="device-name-container">
          <div :class="{ 'device-name': true, 'disconnected': !device.connected }">{{ device.name }}</div>
          <div class="connect-button-container">
            <button v-if="!device.connected" class="connect-button" @click="connectDevice(index)">Connect</button>
            <button v-if="device.connected" class="disconnect-button" @click="disconnectDevice(index)">Disconnect</button>
          </div>
        </div>
        <div class="device-status">
          <div class="led" :class="{ 'red-led': !device.connected, 'green-led': device.connected }"></div>
        </div>
      </li>
    </ul>
    <div class="login-container" v-if="isLoggedIn">
      <div class="login-info">Logged in as {{ currentUser }}</div>
      <button class="logout-button" @click="logout">Log Out</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      devices: [
        { name: 'HIL 1', connected: true },
        { name: 'HIL 2', connected: false },
        { name: 'HIL 3', connected: false }
      ],
      selectedDevice: 0,
      currentUser: null,
      loginUsername: '',
      loginPassword: '',
      loginError: null
    }
  },
  computed: {
    isLoggedIn() {
      return this.currentUser !== null;
    }
  },
  methods: {
    connectDevice(index) {
      // Disconnect the currently connected device, if there is one
      const connectedDeviceIndex = this.devices.findIndex(device => device.connected)
      if (connectedDeviceIndex !== -1) {
        this.devices[connectedDeviceIndex].connected = false
      }

      // Connect the selected device
      this.devices[index].connected = true
    },
    disconnectDevice(index) {
      this.devices[index].connected = false
    },
    login() {
      // Simulate user authentication
      if (this.loginUsername === 'user' && this.loginPassword === 'password') {
        this.currentUser = this.loginUsername;
        this.loginUsername = '';
        this.loginPassword = '';
        this.loginError = null;
      } else {
        this.loginError = 'Invalid username or password.';
      }
    },
    logout() {
      this.currentUser = null;
    }
  }
}
</script>

<style>
.container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #1a1a2e;
}

.login-container {
  position: relative;
  width: 400px;
  height: 400px;
  background-color: #54a1e1;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

input[type="text"], input[type="password"] {
  width: 80%;
  padding: 10px;
  margin: 10px 0;
  border: none;
  border-radius: 20px;
  background-color: rgba(255, 255, 255, 0.2);
  color: #fff;
  font-size: 18px;
  font-weight: 600;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
}

input[type="text"]:focus, input[type="password"]:focus {
  background-color: rgba(255, 255, 255, 0.4);
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
}

button {
  width: 50%;
  padding: 10px;
  margin: 20px 0;
  border: none;
  border-radius: 20px;
  background-color: #54a1e1;
  color: #fff;
  font-size: 18px;
  font-weight: 600;
  cursor: pointer;
  outline: none;
  transition: all 0.3s ease;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
  text-shadow: 0 0 10px rgba(255, 255, 255, 0.4);
}

button:hover {
  background-color: #03dac6;
  box-shadow: 0 0 20px #03dac6;
  text-shadow: 0 0 20px #03dac6;
}

.square {
  position: absolute;
  width: 300px;
  height: 300px;
  background-color: #add8e6;
  opacity: 0.5;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>


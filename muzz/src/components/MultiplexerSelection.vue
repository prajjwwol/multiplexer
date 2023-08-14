<template>
    <div class="multiplexer-selection">
      <h2 class="subtitle">HIL Multiplexer</h2>
      <div class="device-list">
        <device-item
        v-for="device in devices"
        :key="device.id"
        :device="device"
        :is-device-connected="isDeviceConnected"
        @connect-device="connectDevice"
        @disconnect-device="disconnectDevice"
        @sendCommand="sendCommandToDevice"
       ></device-item>
      </div>
      <div class="arduino-status">
        <h3>Arduino Status: {{ arduinoStatus }}</h3>
        <button class="connect-button" :disabled="arduinoStatus === 'Connected'" @click="openConnectionDialog">Connect Arduino</button>
      </div>
      <button class="logout-button" @click="logout">Logout</button>
      <div class="watermark">Designed by PrajjwWol</div>
      <connection-dialog
        v-if="isConnecting"
        @close="closeConnectionDialog"
        @arduino-connection-success="onArduinoConnectionSuccess"
        @arduino-connection-failure="onArduinoConnectionFailure"
      ></connection-dialog>
    </div>
  </template>
  
  <script>
  import DeviceItem from './DeviceItem.vue';
  import ConnectionDialog from './ConnectionDialog.vue';
  import io from 'socket.io-client';
  import axios from 'axios';
  
  export default {
    components: {
      DeviceItem,
      ConnectionDialog,
    },
    data() {
      return {
        devices: [
          { id: 1, name: 'Taikuri', isConnected: false, command: "0,0" },
          { id: 2, name: 'Pikku Myy', isConnected: false, command: "0,1" },
          { id: 3, name: 'Nipsu', isConnected: false, command: "1,0" },
        ],
        arduinoStatus: 'Disconnected',
        isConnecting: false,
        isDeviceConnected: false,
        socket: null,
      };
    },
    created() {
      this.socket = io('http://localhost:8081'); // Replace with your Arduino Create Agent URL
      this.socket.on('connect', () => {
        console.log('Connected to Arduino Create Agent');
        this.arduinoStatus = 'Connected';
      });
      this.socket.on('disconnect', () => {
        console.log('Disconnected from Arduino Create Agent');
        this.arduinoStatus = 'Disconnected';
      });
    },
    methods: {
      connectDevice(device) {
        if (this.isDeviceConnected) return;
  
        this.isDeviceConnected = true;
        this.devices = this.devices.map(d => ({
          ...d,
          isConnected: d.id === device.id,
        }));
      },
      disconnectDevice() {
        this.isDeviceConnected = false;
        this.devices = this.devices.map(d => ({
          ...d,
          isConnected: false,
        }));
      },
      closeConnectionDialog() {
        this.isConnecting = false;
        this.socket.emit('disconnectFromArduino');
      },
      onArduinoConnectionSuccess() {
        this.isConnecting = false;
        this.arduinoStatus = 'Connected'; // Change the status here
      },
      onArduinoConnectionFailure() {
        this.isConnecting = false;
        // Add further actions upon failed connection here
      },
      openConnectionDialog() {
      // Set isConnecting to true to open the Connection Dialog
      this.isConnecting = true;
      },
      async sendCommandToDevice({ device, command }) {
        if (!device || !device.isConnected) return;
          console.log(`Sending command ${command} to device ${device.name}`);
        try {
          const response = await fetch('http://localhost:5000/send_command', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            },
          body: JSON.stringify({ command: device.command }),
        });
          const result = await response.json();
        if (result.success) {
          alert('Command sent successfully');
        } else {
        alert('Failed to send command');
        }
        }catch (error) {
          alert('An error occurred');
      }
      },
      logout() {
        // Logout logic
        // ...
        this.$router.push('/'); // Redirect to the login page
      },
    },
  };
  </script>

<style scoped>
.multiplexer-selection {
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  background: linear-gradient(160deg, #1a242f 0%, #2b3645 100%);
  height: 88vh;
  padding: 2rem;
  color: #0ff0ff;
  font-family: 'Futura', sans-serif; /* Consider using a futuristic font */
  overflow: hidden;
}

.subtitle {
  font-size: 2.5rem;
  margin-bottom: 2rem;
  text-shadow: 0 0 10px #0ff0ff;
}

.device-list {
  display: flex;
  justify-content: center;
  margin-bottom: 2rem;
}

.device-item {
  background: rgba(255, 255, 255, 0.1);
  margin: 0 1rem;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0px 5px 15px 0px rgba(0, 255, 255, 0.5);
  width: 200px;
  transition: all 0.5s ease;
}

.device-item:hover {
  box-shadow: 0px 0px 20px #0ff0ff;
  transform: translateY(-5px);
}

.connect-button, .disconnect-button {
  background-color: #0ff0ff;
  color: #333;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-shadow: 0px 0px 10px #0ff0ff;
  box-shadow: 0px 0px 15px #0ff0ff;
}

.connect-button:hover {
  background-color: #00d9d9;
  box-shadow: 0px 0px 20px #00d9d9;
}

.connect-button:disabled {
  cursor: not-allowed;
  background-color: #999;
}

.disconnect-button {
  background-color: #ff8080;
}

.disconnect-button:hover {
  box-shadow: 0px 0px 20px #ff8080;
}

.arduino-status {
  margin-bottom: 2rem;
  color: #0ff0ff;
  text-shadow: 0px 0px 10px #0ff0ff;
  font-weight: bold;
}

.logout-button {
  background: transparent;
  border: 2px solid #0ff0ff;
  color: #0ff0ff;
  position: absolute;
  bottom: 5rem;
  left: 2rem;
  padding: 1rem;
  border-radius: 15px;
  cursor: pointer;
  transition: all 0.5s ease;
  text-shadow: 0px 0px 10px #0ff0ff;
}

.logout-button:hover {
  background-color: rgba(0, 255, 255, 0.2);
  box-shadow: 0px 0px 20px #ff4d4d;
}

.watermark {
  position: absolute;
  bottom: 5rem;
  right: 10px;
  font-size: 12px;
  color: rgba(51, 51, 255, 0.7);
  font-style: italic;
}

/* Adding a fun background animation */
@keyframes bgAnimation {
  0% {
    background-position: 0 0;
  }
  100% {
    background-position: 100% 100%;
  }
}

body {
  background-size: 200% 200%;
  animation: bgAnimation 15s infinite linear;
  background-image: linear-gradient(45deg, #1a242f, #2b3645, #1a242f, #2b3645);
}
</style>
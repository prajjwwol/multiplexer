<template>
  <div class="device-item" :class="{ connected: device.isConnected }">
    <h3 class="device-name">{{ device.name }}</h3>
    <button
      v-if="!device.isConnected"
      class="connect-button"
      :disabled="isDeviceConnected && !device.isConnected" 
      @click="sendCommand('Connect')"
    >Connect</button>
    <button
      v-if="device.isConnected"
      class="disconnect-button"
      @click="sendCommand('Disconnect')"
    >Disconnect</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['device', 'isDeviceConnected'],
  methods: {
    async sendCommand(action) { 
      try {
        // Mapping device names to commands
        const commandsMap = {
          'Disconnect': '0,0', // Disconnect command for all devices
          'Taikuri': '0,1',
          'Pikku Myy': '1,0',
          'Nipsu': '1,1',
        };

        // If the action is "Connect", use the device name, otherwise use "Disconnect"
        const commandKey = action === 'Connect' ? this.device.name : 'Disconnect';
        
        const command = commandsMap[commandKey];
        if (!command) {
          console.error('Unknown device');
          return;
        }

        // Send the specific command for this device
        const responseSend = await axios.post('http://192.168.37.239:5000/send_command', { command });
        if (responseSend.data.success) {
          console.log('Command sent successfully');
          this.$emit(action === 'Connect' ? 'connect-device' : 'disconnect-device', this.device);
        } else {
          console.error('Failed to send command');
        }
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>


<style scoped>
.device-item {
  background-color: #333;
  margin: 1rem;
  padding: 1rem;
  border-radius: 10px;
  box-shadow: 0px 0px 20px #0cf;
  transition: box-shadow 0.3s ease;
  width: 300px;
  text-align: center;
}

.device-item.connected {
  opacity: 0.5;
}

.device-name {
  color: #fff;
  font-size: 2rem;
  margin-bottom: 1rem;
  text-shadow: 0px 0px 10px #0cf;
}

.connect-button, .disconnect-button {
  background-color: #00f7ff; /* Neon Blue */
  border: none;
  color: #000;
  padding: 0.5rem 1rem;
  border-radius: 5px;
  margin-bottom: 1rem;
  width: 100%;
  box-shadow: 0px 5px 10px 0px rgba(0, 247, 255, 0.8); /* Neon Blue */
  transition: box-shadow 0.3s ease;
  text-shadow: 0px 0px 10px #00f7ff; /* Neon Blue */
}

.connect-button:hover {
  box-shadow: 0px 5px 20px 0px rgba(0, 247, 255, 0.8); /* Neon Blue */
}

.connect-button:disabled {
  background-color: #888; /* Gray */
  cursor: not-allowed;
  box-shadow: none;
}

.disconnect-button {
  background-color: #ff4d4d; /* Neon Red */
}

.connect-button:disabled:hover {
  box-shadow: none;
}

.disconnect-button:hover {
  box-shadow: 0px 5px 20px 0px rgba(255, 77, 77, 0.8); /* Neon Red */
}
</style>


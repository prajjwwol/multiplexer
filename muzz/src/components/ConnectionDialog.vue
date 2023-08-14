<template>
    <div v-if="isVisible" class="connection-dialog">
      <h3>Connect to Arduino</h3>
      <div v-if="isConnecting">
        <p>Connecting...</p>
      </div>
      <div v-else-if="isConnected">
        <p>Connected to Arduino at {{ comPort }}</p>
        <button @click="disconnectFromArduino">Disconnect</button>
      </div>
      <div v-else>
        <button @click="connectToArduino">Connect</button>
      </div>
      <button @click="close">Close</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: ['isVisible'],
    data() {
      return {
        isConnected: false,
        isConnecting: false,
        comPort: '',
      };
    },
    methods: {
      async connectToArduino() {
        this.isConnecting = true;
        try {
          const response = await axios.post('http://192.168.37.239:5000/connect');
          if (response.data.success) {
            this.isConnected = true;
            this.comPort = response.data.comPort;
            this.isConnecting = false;
            this.$emit('arduino-connection-success');
          } else {
            this.isConnecting = false;
            this.$emit('arduino-connection-failure');
          }
        } catch (error) {
          this.isConnecting = false;
          console.error('Error:', error);
        }
      },
      async disconnectFromArduino() {
        this.isConnected = false;
        this.$emit('disconnect-arduino');
      },
      close() {
        this.$emit('close-dialog');
      },
    },
  };
  </script>
  
  <style scoped>
  .connection-dialog {
    display: flex;
    justify-content: center;
    align-items: center;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7); /* Darker overlay */
  }
  
  .content {
    background-color: #1a1a1a; /* Darker background color */
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    position: relative;
    width: 400px;
    box-shadow: 0px 0px 40px #00f7ff; /* Neon glow effect */
  }
  
  .close-button-container {
    position: absolute;
    top: 10px;
    right: 10px;
    
  }
  
  .connecting-icon {
    display: flex;
    align-items: center;
    margin-bottom: 2rem;
  }
  
  .pc-icon,
  .arduino-icon {
    width: 80px;
  }
  
  
  .title {
    color: #00f7ff; /* Neon Blue */
    font-size: 2rem;
    margin-bottom: 1rem;
    text-shadow: 0px 0px 10px #00f7ff; /* Neon text effect */
  }
  
  .connecting-container {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    margin-bottom: 2rem;
  }
  
  .loading-animation {
    width: 60px;
    height: 16px;
    display: flex;
    justify-content: space-between;
  }
  
  .loading-animation div {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #00f7ff; /* Neon Blue */
    animation: neon-loading 1s infinite;
  }
  
  .loading-animation div:nth-child(1) {   /* dots */
    animation-delay: 0s;
  }
  
  .loading-animation div:nth-child(2) {
    animation-delay: 0.2s;
  }
  
  .loading-animation div:nth-child(3) {
    animation-delay: 0.4s;
  }
  
  @keyframes neon-loading {   /*dots moving */
    0% {
      opacity: 0.3;
      transform: scale(1);
    }
    50% {
      opacity: 1;
      transform: scale(1.3);
    }
    100% {
      opacity: 0.3;
      transform: scale(1);
    }
  }
  
  .success-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .success-icon {
    width: 80px;
  }
  
  .close-button {
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
  
  .connecting-icon {
    display: flex;
    align-items: center;
    justify-content: space-evenly; 
    margin-bottom: 5rem;
  }
  
  .close-button:hover {
    color: #ff4d4d;
    box-shadow: 0px 5px 20px 0px rgba(255, 77, 77, 0.8); /* Neon Red */
    
  }
  
  .retry-button {
    background-color: #00f7ff; /* Neon Blue */
    border: none;
    color: #000;
    padding: 0.5rem 1rem; /*  size  */
    border-radius: 5px;
    margin-bottom: 1rem;
    width: 25%;
    box-shadow: 0px 5px 10px 0px rgba(0, 247, 255, 0.8); /* Neon Blue */
    transition: box-shadow 0.3s ease;
    text-shadow: 0px 0px 10px #00f7ff; /* Neon Blue */
  }
  
  .retry-button:hover {
    box-shadow: 0px 5px 20px 0px rgba(0, 247, 255, 0.8); 
  }
  
  .failed-container {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .failed-message {
    color: #ff0000;
    font-size: 2rem;
    margin-bottom: 1rem;
    text-shadow: 0px 0px 5px #ff0000; /* Red glow effect */
  }
  
  
  .com-port {
    color: #0cf;
    font-size: 1.2rem;
    margin-bottom: 1rem;
    text-shadow: 0px 0px 5px #0cf; /* Blue glow effect */
  }
  
  </style>
  
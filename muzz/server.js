const express = require('express');
const https = require('https');
const socketIO = require('socket.io');
const fs = require('fs');
const path = require('path');
const five = require('johnny-five');

const app = express();

// Read the SSL/TLS certificates
const privateKeyPath = path.join(__dirname, 'server.key');
const certificatePath = path.join(__dirname, 'server.cert');

const privateKey = fs.readFileSync(privateKeyPath, 'utf8');
const certificate = fs.readFileSync(certificatePath, 'utf8');

const credentials = { key: privateKey, cert: certificate };

// Create an HTTPS server
const server = https.createServer(credentials, app);

const io = socketIO(server);

// Set up CORS middleware to allow requests from all origins
const cors = require('cors');
app.use(cors());

// Define a route to serve the Vue.js application
app.use('/', express.static(path.join(__dirname, 'dist')));

// Handle WebSocket connections
io.on('connection', (socket) => {
  console.log('A client connected:', socket.id);

  // Connect to the Arduino Uno WiFi via serial port (COM9)
  const board = new five.Board({
    port: 'COM9', // Adjust the COM port name according to your setup
  });

  // Rest of your WebSocket code remains the same ...

  // Handle disconnection
  socket.on('disconnect', () => {
    console.log('A client disconnected:', socket.id);
  });
});

const port = 8081;
server.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

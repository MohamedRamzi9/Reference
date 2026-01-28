// how to use WebSocket api in JavaScript

// create a new WebSocket connection by specifying the URL of the server
const socket = new WebSocket('ws://localhost:1234');

// set the on connection open function (this is called when the connection is established)
socket.onopen = () => {
  console.log('WebSocket connection opened');
}

// set the on message function (this is called when a message is received from the server)
socket.onmessage = (event) => {
  console.log('Message from server:', event.data);
}

// set the on error function (this is called when an error occurs)
socket.onerror = (error) => {
  console.error('WebSocket error:', error);
}

// set the on connection close function (this is called when the connection is closed)
socket.onclose = () => {
  console.log('WebSocket connection closed');
}

// send a message to the server
socket.send('Hello, server!');

// close the WebSocket connection
socket.close();
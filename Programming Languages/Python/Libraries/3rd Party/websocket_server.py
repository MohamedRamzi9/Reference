
import websocket_server

# on new client function
def new_client(client, server):
	# get the client id
	print("New client connected: %s" % client['id'])
	# send a message to the client
	server.send_message(client, "Welcome to the WebSocket server!")
	# broadcast a message to all other clients
	for c in server.clients:
		if c != client:
			server.send_message(c, "New client connected: %s" % client['id'])

# on recieve message function
def message_received(client, server, message):
	print("Message from client %s: %s" % (client['id'], message))
	# send a message to the client
	server.send_message(client, "Message received: %s" % message)
	# broadcast a message to all other clients
	for c in server.clients:
		if c != client:
			server.send_message(c, "Message from client %s: %s" % (client['id'], message))

# on client disconnect function
def client_disconnected(client, server):
	print("Client disconnected: %s" % client['id'])
	# broadcast a message to all other clients
	for c in server.clients:
		if c != client:
			server.send_message(c, "Client disconnected: %s" % client['id'])

# create a new websocket server by passing the host and port
server = websocket_server.WebsocketServer(host='localhost', port=8080)
# set the new client function
server.set_fn_new_client(new_client)
# set the message received function
server.set_fn_message_received(message_received)
# set the client disconnected function
server.set_fn_client_left(client_disconnected)
# start the server (this will block the current thread in an infinite loop)
server.run_forever()

# Chatroom Application

## Introduction
This is a simple chatroom application implemented in Python using the websockets library. It consists of a server and a client component, allowing users to connect, exchange messages, and chat in real-time. The server runs a WebSocket server, while the client can connect to it and participate in the chat.

## Usage
### Server
1. Start the server by running the `server.py` script.
2. The server will listen on "localhost" at port 8765.
3. Users can connect to the server and enter their names.
4. Once connected, they can send and receive messages in the chatroom.

### Client
1. Run the `client.py` script to start the client.
2. The client will prompt you to enter your name.
3. After entering your name, you will receive a welcome message.
4. You can send messages by typing and pressing Enter.
5. To exit the chat, simply type 'exit' and press Enter.

## Safety Concerns
- **Data Privacy:** This application does not provide any form of encryption or authentication. Messages are transmitted in plain text, which could be intercepted by malicious users on the network. Avoid sharing sensitive information.
- **Error Handling:** The application does basic error handling but might not handle all possible exceptions. If the server crashes or the client encounters an error, it may not gracefully recover.

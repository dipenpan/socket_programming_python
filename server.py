# Dipendra Pandey
import socket

def server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_socket.bind(('localhost', 8080))  # Replace with your desired IP and port
    
    # Listen for incoming connections
    server_socket.listen(5)
    print("Server is listening on localhost:8080")
    
    try:
        while True:
            # Accept a new connection from a client
            client_socket, addr = server_socket.accept()
            print(f"Connection established from {addr}")
            
            # Handle communication with this client
            handle_client(client_socket, addr)
    except KeyboardInterrupt:
        print("Server shutting down")
    finally:
        server_socket.close()

def handle_client(client_socket, addr):
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode()
            
            # If no message received, client has closed the connection
            if not message:
                break
                
            print(f"Received from {addr}: {message}")
            
            # Check if client wants to quit
            if message.lower() == 'quit':
                client_socket.send("Connection terminated by client.".encode())
                break
                
            # Send response back to client
            response = f"Server received: {message}"
            client_socket.send(response.encode())
    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        print(f"Connection with {addr} closed")

if __name__ == "__main__":
    server()
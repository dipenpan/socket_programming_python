# Dipendra Pandey
import socket

def client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define the server address and port to connect to
    server_host = 'localhost'
    server_port = 8080
    
    try:
        # Connect to the server
        client_socket.connect((server_host, server_port))
        print(f"Connected to server at {server_host}:{server_port}")
        print("Type 'quit' to end the connection")
        
        # Loop to send multiple messages
        while True:
            # Get message from user
            message = input("Enter message to send: ")
            
            # Send message to server
            client_socket.send(message.encode())
            
            # Check if user wants to quit
            if message.lower() == 'quit':
                break
                
            # Receive and display the server's response
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
            
    except ConnectionRefusedError:
        print("Failed to connect to the server. Make sure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    client()
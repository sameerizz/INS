import socket
import ssl

# Create SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="localhost.crt", keyfile="localhost.key")

# Create and configure server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("", 4434))
    server.listen(5)
    print("Server ready and listening for connections")

    # Wait for new connections in a loop
    while True:
        sock, address = server.accept()
        print(f"New connection from {address[0]}:{address[1]}")

        # Wrap socket with SSL
        ssl_sock = context.wrap_socket(sock, server_side=True)

        while True:
            # Receive data from client
            data = ssl_sock.recv(1024)
            
            # Decode byte array to utf-8 string
            decoded = data.decode('utf-8')

            # Close the socket if the client sends empty bytes
            if decoded == "":
                break
            
            # Log what the client sends
            print(f"[{address[0]}:{address[1]}] {decoded}")

            # Echo the data back to the client
            ssl_sock.sendall(data)

        # Gracefully close the connection and wait for next one
        print(f"Closing connection with {address[0]}:{address[1]}")
        ssl_sock.close()
import socket
import ssl

# Create a socket and set timeout
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(10)

    # Wrap socket with SSL
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('localhost.crt')

    ssl_sock = context.wrap_socket(sock, server_hostname="localhost")

    # Connect to the server
    ssl_sock.connect(("localhost", 4434))
    print("Connected to server")

    # Send input data to server and wait for response in a loop
    while True:
        ssl_sock.sendall(bytes(input("> "), "utf-8"))
        data = ssl_sock.recv(1024)
        print("Server responded:", data.decode('utf-8'))
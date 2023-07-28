import socket
from rsa import decrypt

# Define server IP address and port
HOST = '0.0.0.0'
PORT = 12346

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

# Wait for a client to connect
print('Waiting for client connection...')
client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

# Receive Private key from the client
private_key = client_socket.recv(1024)
private_key = eval(private_key)

# Receive data from the client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    data = data.decode('utf-8')
    # Decrypt the message
    data, md5_checksum = data.split("|")
    data = eval(data)
    decrypted = decrypt(private_key, data, md5_checksum)
    print('Decrypted:', decrypted)

# Close the connection
client_socket.close()

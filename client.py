import socket
from rsa import encrypt, generate_keypair

# Define server IP address and port
HOST = '127.0.0.1'
PORT = 12346

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))
print('Connected to server')

# Encryption 
p = 61
q = 53
# public_key = (17, 3233)
public_key, private_key = generate_keypair(p, q)
private_key = f"{private_key}"
client_socket.sendall(private_key.encode('utf-8'))

# Send data to the server
msg = ''
while msg != 'bye':
    msg = input()
    encrypted, md5_checksum = encrypt(public_key, msg)
    # Send the encrypted message to the server
    total_data = encrypted + "|" + md5_checksum
    client_socket.sendall(total_data.encode('utf-8'))

# Close the connection
client_socket.close()

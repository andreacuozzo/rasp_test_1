import socket
import sys
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('192.168.1.19', 10002)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received ' + data
            if data:
                if data[0:4] == 'cent':
                    os.system('ola_streaming_client -u 1 -d 85,,50')
                if data[0:4] == 'drit':
                    os.system('ola_streaming_client -u 1 -d 70,,50')
                if data[0:4] == 'rove':
                    os.system('ola_streaming_client -u 1 -d 100,,50')
                if data[0:4] == 'lobc':
                    os.system('ola_streaming_client -u 1 -d 85,,80')
                if data[0:4] == 'lobd':
                    os.system('ola_streaming_client -u 1 -d 70,,80')
                if data[0:4] == 'lobr':
                    os.system('ola_streaming_client -u 1 -d 100,,80')
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()
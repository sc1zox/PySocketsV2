import socket

server_address = '127.0.0.1',4000
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(server_address)

try:
    message = 'hello can you hear me'
    message_encoded = message.encode('utf-8')
    sock.send(message_encoded)

    response = sock.recv(4096)
    response_decoded = response.decode('utf-8')

    print(f'send: {message}')

    print(f'The server said: {response_decoded}')

finally:
    sock.close()
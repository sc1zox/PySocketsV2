import socket

server_address = ('127.0.0.1',4001)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(server_address)

try:
    while True:
        print(f'server is running on: {server_address}')
        response, client_addr = sock.recvfrom(4096)
        response_decoded = response.decode('utf-8')

        print(f' the message was {response_decoded}')
        message = 'udp sucks'
        print(f'sending.... {message}')
        message_encoded = message.encode('utf-8')

        sock.sendto(message_encoded, client_addr)

except KeyboardInterrupt:
    print('stopped')
finally:
        sock.close()
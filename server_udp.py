import socket

server_address = ('127.0.0.1',4000)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(server_address)

while True:
    try:
        print(f'server is running on: {server_address}')
        response, client_addr = sock.recvfrom(4096)
        response_decoded = response.decode('utf-8')

        print(f' the response was {response_decoded}')
        message = 'udp sucks'
        message_encoded = message.encode('utf-8')

        sock.sendto(message_encoded, client_addr)

    except KeyboardInterrupt:
        break
    finally:
        sock.close()
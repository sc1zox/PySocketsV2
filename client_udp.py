import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('127.0.0.1',4712)

try:
    message = 'Hello I need Hello - wat'
    message_encoded = message.encode('utf-8')

    print(f'sending: {message} to {server_address}')

    sock.sendto(message_encoded,server_address)

    response,address = sock.recvfrom(4096)
    response_decoded = response.decode('utf-8')

    print(f'server said: {response_decoded} from {address}')

except KeyboardInterrupt:
    print('client stopped')

finally:
    print('client done')
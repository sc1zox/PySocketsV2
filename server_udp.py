import socket

server_address = ('127.0.0.1',4712)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(server_address)
print('running')

try:
    while True:
        msg, addr = sock.recvfrom(4096)

        msg_dc = msg.decode('utf-8')
        print(f'{msg_dc}')

        msg_new = 'fk this'.encode('utf-8')

        sock.sendto(msg_new,addr)

except KeyboardInterrupt:
    print('server stopped')

sock.close()
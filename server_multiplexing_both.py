import select
import socket

udp = ('127.0.0.1',4712)
tcp = ('127.0.0.1',4001)

socket_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
socket_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_udp.bind(udp)
socket_tcp.bind(tcp)
socket_tcp.listen()

print(f'UDP läuft: {udp}')
print(f'TCP läuft: {tcp}')

socket_list = [socket_udp,socket_tcp]
while True:
    try:
        readable,_,_ = select.select(socket_list,[],[])
        for socket in readable:
            if socket == socket_udp:
                response, address = socket.recvfrom(4096)
                response_decoded = response.decode('utf-8')
                print(f'Client said {response_decoded} from {address}')

                message = 'udp is dope'
                message_encoded = message.encode('utf-8')
                socket.sendto(message_encoded,address)
            else:
                connection, address = socket_tcp.accept()

                response = connection.recv(4096)
                response_decoded = response.decode('utf-8')
                print(f'Client said {response_decoded} from {address}')

                message = 'No, hello can you hear me?'
                message_encoded = message.encode('utf-8')

                connection.send(message_encoded)
    except KeyboardInterrupt:
        print('stopped server')
        break
    except Exception as e:
        print(f"Fehler: {e}")

socket_tcp.close()
socket_udp.close()


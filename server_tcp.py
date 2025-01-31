import socket

server_data = ('127.0.0.1',3000)

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(server_data)
sock.listen()

print("TCP server running")

while True:
    try:
        connection, sender_address = sock.accept()
        data = connection.recv(4096)
        if not data:
            break
        decoded_message = data.decode('utf-8')
        print(f"recieved from: {sender_address} with the message: {decoded_message}")

        response = 'Fuck you'
        response_encoded = response.encode('utf-8')
        connection.send(response_encoded)

    except KeyboardInterrupt:
        print('Server shut down')
        break
    finally:
        connection.close()

sock.close()
import concurrent.futures.thread
import socket


def handle_client_tcp(connection, address):
    try:
        response = connection.recv(4096)
        response_decoded = response.decode('utf-8')

        print(f'TCP sagt: {response_decoded} von {address}')

        message = 'Waddup tcp'
        message_decoded = message.encode('utf-8')

        connection.send(message_decoded)
    except Exception as e:
        print(f"Fehler bei TCP-Verarbeitung: {e}")
    finally:
        connection.close()

def start_server():
    server_tcp = ('127.0.0.1', 4000)
    sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_tcp.bind(server_tcp)
    sock_tcp.listen()

    print(f'TCP server läuft auf {server_tcp}')

    with concurrent.futures.thread.ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            try:
                connection, addr_tcp = sock_tcp.accept()
                executor.submit(handle_client_tcp,connection, addr_tcp)

            except KeyboardInterrupt:
                print("\nServer wird geschlossen.")
                break
            except Exception as e:
                print(f"Fehler: {e}")



if __name__ == '__main__':
    start_server()
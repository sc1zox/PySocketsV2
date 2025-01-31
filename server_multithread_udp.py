import concurrent.futures.thread
import socket



def handle_client_udp(sock,response, address):
    try:
        response_decoded = response.decode('utf-8')
        print(f'UDP Gerade reingekommen: {response_decoded}')

        message = 'check habibi'
        message_encoded = message.encode('utf-8')
        sock.sendto(message_encoded,address)
    except Exception as e:
        print(f"Fehler bei TCP-Verarbeitung: {e}")


def start_server():
    server_udp = ('127.0.0.1', 4712)
    sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_udp.bind(server_udp)

    print(f'UDP server läuft auf {server_udp}')

    with concurrent.futures.thread.ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            try:
                response, addr_udp = sock_udp.recvfrom(4096)
                executor.submit(handle_client_udp,sock_udp,response, addr_udp)

            except KeyboardInterrupt:
                print("\nServer wird geschlossen.")
                break
            except Exception as e:
                print(f"Fehler: {e}")

if __name__ == '__main__':
    start_server()
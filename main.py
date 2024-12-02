import socket

def run_udp_server(host='127.0.0.1', port=65432):

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((host, port))

        while True:
            print("Ожидание")
            data, addr = server_socket.recvfrom(1024)
            print(f"Получено сообщение: {data.decode('utf-8')}")


            server_socket.sendto(data, addr)
            print(f"Сообщение отправлено обратно клиенту")

if __name__ == "__main__":
    run_udp_server()


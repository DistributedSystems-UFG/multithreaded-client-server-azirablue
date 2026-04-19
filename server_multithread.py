from socket import *
from constCS import *
import threading
import time


def process_request(msg):
    parts = msg.split(" ", 1)
    command = parts[0].upper()

    if len(parts) > 1:
        data = parts[1]
    else:
        data = ""

    if command == "UPPER":
        return data.upper()
    elif command == "LOWER":
        return data.lower()
    elif command == "REVERSE":
        return data[::-1]
    elif command == "COUNT":
        return str(len(data))
    else:
        return "Comando inválido"


def recv_msg(conn):
    data = b""
    while not data.endswith(b"\n"):
        chunk = conn.recv(1024)
        if not chunk:
            return None
        data += chunk
    return data.decode().strip()


def handle_client(conn, addr):
    print(f"Cliente conectado: {addr}")
    while True:
        msg = recv_msg(conn)
        if msg is None:
            break

        start_time = time.time()
        print(f"Recebido de {addr}: {msg}")
        response = process_request(msg)
        processing_time = time.time() - start_time

        full_response = f"{response} | tempo servidor: {processing_time:.6f}s\n"
        conn.send(full_response.encode())

    conn.close()
    print(f"Conexão encerrada: {addr}")


server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(100)

print("Servidor multithread aguardando conexões...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.daemon = True
    thread.start()

from socket import *
from constCS import *
import random
import string
import time

TOTAL_REQUISICOES = 500

def random_text(size=10):
    return ''.join(random.choices(string.ascii_letters, k=size))


def generate_request():
    commands = ["UPPER", "LOWER", "REVERSE", "COUNT"]
    command = random.choice(commands)
    text = random_text()
    return f"{command} {text}"


def recv_msg(s):
    data = b""
    while not data.endswith(b"\n"):
        chunk = s.recv(1024)
        if not chunk:
            break
        data += chunk
    return data.decode().strip()


experiment_start = time.time()

for i in range(TOTAL_REQUISICOES):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))

    request = generate_request()
    start_time = time.time()

    s.send((request + "\n").encode())
    response = recv_msg(s)

    end_time = time.time()
    print(f"Req {i+1}: {request} -> {response} | tempo: {end_time-start_time:.6f}s")

    s.close()

experiment_end = time.time()
print(f"\nTempo total: {experiment_end - experiment_start:.6f}s")

import socket
import sys
import time

HOST, PORT = "127.0.0.1", 8999
STATE_UDP_PORT = 8890
data = " ".join(sys.argv[1:])


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, 0))

received = str(sock.recv(1024), "utf-8")
sock.sendto(bytes(data, "utf-8"), (HOST, PORT))

print(f"Sent:     {data}")
print(f"Received: {received}")
time.sleep(4)
state_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
state_socket.bind(("", STATE_UDP_PORT))

while True:
    data, address = state_socket.recvfrom(1024)
    address = address[0]
    print(f'Data received from {address} at state_socket')

    print("Data:", data.decode('ASCII'))

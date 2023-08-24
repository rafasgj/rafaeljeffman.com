import socket
import select
import sys


def chat_client(conn, addr):
    client_connected = conn is not None
    try:
        while client_connected:
            message = conn.recv(2048).decode("utf-8")
            if message:
                print(f"<{addr}>: {message}")
                conn.send("200 OK Message received.".encode("utf-8"))
            else:
                client_connected = False
    except Exception as ex:
        print("ERROR: ", ex)
    conn.close()
        

port = int(sys.argv[1]) if len(sys.argv) > 1 else 19000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('0.0.0.0', port))

server.listen(5)

running = True
while running:
    conn, addr = server.accept()

    chat_client(conn, addr)

server.close()

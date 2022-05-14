import socket
import threading
import random

flag = "VHC2022{B1n4ry_0v3rd0s3d!}"

bindIp = "0.0.0.0"
bindPort = 1010

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bindIp, bindPort))
server.listen(10)

minVal = 0
maxVal = 18446744073709551616

message = "I have created a number 0 <= x <= 18446744073709551616. Can you guess it???\nRemember you only have 70 tries :)\nAnd just 2 seconds per trial!\n"

def handleClient(clientSocket):
    clientSocket.send(message.encode())
    time = 70
    result = random.randrange(minVal, maxVal)
    while time > 0:
        try:
            clientSocket.settimeout(2)
            recv = int(clientSocket.recv(1024).decode())
            time -= 1
            if (recv == result):
                clientSocket.send("Yay! you got the true number! {}\n".format(flag).encode())
                clientSocket.close()
                return
            if (recv < result):
                clientSocket.send("Ehm... a bit HIGHER!. You got {} trials left.\n".format(time).encode())
                continue
            if (recv > result):
                clientSocket.send("Ehm... a bit LOWER! You got {} trials left.\n".format(time).encode())
                continue
        except:
            clientSocket.send("You are either too slow or too bad at handling...\n".encode())
            clientSocket.send("You should type faster :)\n".encode())
            clientSocket.close()
            return
    clientSocket.send("OH NO :) No trials left. Byebye!\n".encode())
    return

while True:
    client, addr = server.accept()
    clientHandler = threading.Thread(target = handleClient, args = (client,))
    clientHandler.start()
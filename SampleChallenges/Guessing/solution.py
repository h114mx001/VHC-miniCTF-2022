import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("167.172.16.55",1010))\

data = s.recv(10240).decode() #receive the notification
print(data)

l = 0
r = 18446744073709551616

while True:
    m = (l + r) // 2;
    s.send((str(m)+'\n').encode())
    print(m)
    data = s.recv(10240).decode()
    print(data) 
    data = data.split()[3]
    print(data)
    if (data == "LOWER!"): r = m-1 # too high -> the answer is strictly less than m
    else: l = m + 1; # too low -> the answer is strictly larger than m

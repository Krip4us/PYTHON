import socket
hostname = socket.gethostname()
Ipaddr = socket.gethostbyname(hostname)
print("my ip is : " + Ipaddr)

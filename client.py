import http.client
import socket

con = http.client.HTTPConnection("127.0.0.1:8888", timeout=10)
con.request("GET", "/port", headers={"Content-type": "text/html"})
print(1)
res = con.getresponse()
print(2)
res.read()
if res.status == 200:
    print("200 ok")
    port_num = int(res.read().decode())
    print(f'port number is {port_num}')
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    c.connect(('127.0.0.1', port_num))
    while True:
        code = input("Enter code: ")
        c.sendto(code.encode(), ('127.0.0.1', port_num))
        answer = c.recv(1024, socket.MSG_DONTWAIT).decode()
        print(answer)
else:
    print("Error: ", res.status, res.reason)
con.close()

import http.server
import random
import socket


class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("in get")
        if self.path == '/port':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            port_num = random.randint(1, 65535)
            self.wfile.write(str(port_num).encode())
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.bind(('127.0.0.1', port_num))
            data, addr = s.recvfrom(1024)
            if data.decode() == "Cyber Himmelfarb":
                s.sendto("Victory!".encode(), addr)
            else:
                s.sendto("No Entry".encode(), addr)
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=http.server.HTTPServer, handler_class=RequestHandler, port=8888):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run()

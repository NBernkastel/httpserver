from jinja2 import Environment, FileSystemLoader
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()


class HttpGetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        f = open("index.html", 'r')
        self.wfile.write(f.read().encode())

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(post_data.decode('utf-8'))
        env = Environment(loader=FileSystemLoader("."))
        templ = env.get_template("temp.html")
        f = open(file="index.html", mode='w')
        di = eval(post_data.decode('utf-8'))
        f.write(templ.render(di))
        f.close()


run(handler_class=HttpGetHandler)
# env = Environment(loader=FileSystemLoader("."))
# templ = env.get_template("temp.html")
# f = open(file="index.html", mode='w')
# di = {"id": 10}
# f.write(templ.render(di))
# f.close()

from http.server import HTTPServer

from controllers.IndexController import IndexController

def run(server_class=HTTPServer, handler_class=IndexController, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
from http.server import BaseHTTPRequestHandler
import json

class UserController(BaseHTTPRequestHandler):
    users = {}

    def do_GET(self):
        path = self.path.split('/')
        if len(path) != 3 or not path[2].isdigit():
            self.send_response(400)
            self.end_headers()
            return

        user_id = int(path[2])
        if user_id not in self.users:
            self.send_response(404)
            self.end_headers()
            return

        user_data = self.users[user_id]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(user_data).encode())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_data = json.loads(post_data)

        user_id = len(self.users) + 1
        self.users[user_id] = user_data

        self.send_response(201)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'id': user_id, 'message': 'User created'}
        self.wfile.write(json.dumps(response).encode())

    def do_PUT(self):
        path = self.path.split('/')
        if len(path) != 3 or not path[2].isdigit():
            self.send_response(400)
            self.end_headers()
            return

        user_id = int(path[2])
        if user_id not in self.users:
            self.send_response(404)
            self.end_headers()
            return

        content_length = int(self.headers['Content-Length'])
        put_data = self.rfile.read(content_length)
        user_data = json.loads(put_data)

        self.users[user_id] = user_data

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'id': user_id, 'message': 'User updated'}
        self.wfile.write(json.dumps(response).encode())

    def do_DELETE(self):
        path = self.path.split('/')
        if len(path) != 3 or not path[2].isdigit():
            self.send_response(400)
            self.end_headers()
            return

        user_id = int(path[2])
        if user_id not in self.users:
            self.send_response(404)
            self.end_headers()
            return

        del self.users[user_id]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {'id': user_id, 'message': 'User deleted'}
        self.wfile.write(json.dumps(response).encode())
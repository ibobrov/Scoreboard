from http.server import BaseHTTPRequestHandler

from app.controllers.IndexController import IndexController
from app.controllers.Router import Router
from app.controllers.UserController import UserController

router = Router()
router.add_route('/', IndexController)
router.add_route('/users', UserController)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        handler_class = router.get_handler(self.path)
        if handler_class:
            handler = handler_class(self.request, self.client_address, self.server)
            handler.do_GET()
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not Found')
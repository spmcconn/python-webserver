import tornado.ioloop
import tornado.web
import tornado.websocket
import os.path

# Tornado Folder Paths
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
)

# Tonado server port
PORT = 80


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("[HTTP](MainHandler) User Connected.")
        self.render("index.html")

class PostHandler(tornado.web.RequestHandler):
    def post(self):
        # user = self.get_argument("username")
        print("[HTTP](PostHandler) Post Request: ", self.get_argument("date"))
        self.write("OK")

class WSHandler(tornado.websocket.WebSocketHandler):
    connections = set()

    def open(self):
        self.connections.add(self)

    def on_message(self, message):
        print('[WS] Incoming message:', message)
        # Broadcast message to all clients
        [client.write_message(message) for client in self.connections]

    def on_close(self):
        print('[WS] Connection was closed.')
        self.connections.remove(self)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/post", PostHandler),
        (r"/ws", WSHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()

import helpers
import tornado.ioloop
import tornado.web
import tornado.websocket
import os.path
import json

# Tornado Folder Paths
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
)

# Tonado server port
PORT = 81

connections = set()

def getItems(file_path):
    f = open(file_path, "r")
    lines = f.readlines()

    length = 5 if len(lines) >= 5 else len(lines)
    items = lines[-length:] if length > 0 else []

    return items

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("[HTTP](MainHandler) User Connected.")

        nick_items = getItems("/home/pi/nick.txt")

        self.render("index2.html", nick_items = nick_items)


class WSHandler(tornado.websocket.WebSocketHandler):
    global connections

    def open(self):
        connections.add(self)

    def on_message(self, message):
        print('[WS] Incoming message:', message)

        date = helpers.get_time_now()

        f = open("/home/pi/" + message + ".txt", "a")
        f.write(date + "\n")
        f.close()

        # Broadcast message to all clients
        [client.write_message({"date": date, "list": message}) for client in connections]

    def on_close(self):
        print('[WS] Connection was closed.')
        connections.remove(self)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/ws", WSHandler),
        (r'/static/(.*)', tornado.web.StaticFileHandler),
    ], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(PORT)
    tornado.ioloop.IOLoop.current().start()

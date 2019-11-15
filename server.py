import tornado.ioloop
import tornado.web
import tornado.websocket
import os.path
import json
from datetime import datetime

# Tornado Folder Paths
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")
)

# Tonado server port
PORT = 80

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

        addison_items = getItems("/home/pi/addison.txt")
        andi_items = getItems("/home/pi/andi.txt")
        kitties_items = getItems("/home/pi/kitties.txt")

        # addison_items = getItems("addison.txt")
        # andi_items = getItems("andi.txt")
        # kitties_items = getItems("kitties.txt")

        self.render("index.html", addison_items = addison_items, andi_items = andi_items, kitties_items = kitties_items)


class PostHandler(tornado.web.RequestHandler):
    def post(self):
        # user = self.get_argument("username")
        print("[HTTP](PostHandler) Post Request: ", self.get_argument("date"))

        f = open("/home/pi/" + self.get_argument("list") + ".txt", "a")
        f.write(self.get_argument("date") + "\n")
        f.close()

        [client.write_message({"date": self.get_argument("date"), "list": self.get_argument("list")}) for client in connections]
        self.write("OK")


class WSHandler(tornado.websocket.WebSocketHandler):
    # connections = set()
    global connections

    def open(self):
        # self.connections.add(self)
        connections.add(self)

    def on_message(self, message):
        print('[WS] Incoming message:', message)

        date = datetime.now().strftime("%A, %B %d %Y %H:%M")

        f = open("/home/pi/" + message + ".txt", "a")
        f.write(date + "\n")
        f.close()

        # Broadcast message to all clients
        # [client.write_message(message) for client in self.connections]
        [client.write_message({"date": date, "list": message}) for client in connections]

    def on_close(self):
        print('[WS] Connection was closed.')
        # self.connections.remove(self)
        connections.remove(self)


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

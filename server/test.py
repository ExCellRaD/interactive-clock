import tornado.ioloop
import tornado.web
from strandtest import Ledstrip
from quickstart import Data

data = Data();
data.main();

ledstrip = Ledstrip()



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = ["Item 1", "Item 2", "Item 3"]
        self.render("test.html", title="My Clock", items=items)

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()

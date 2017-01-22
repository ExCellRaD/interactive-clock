import tornado.ioloop
import tornado.web
from quickstart import Data


#ledstrip = Ledstrip()



class MainHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("test.html", title="My Clock" )

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()

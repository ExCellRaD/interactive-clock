import tornado.ioloop
import tornado.web
from ledtest import Led
from quickstart import Data


data = Data()

results = data.main()
calenderlist = data.getCalenderList()

#ledstrip = Ledstrip()



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        items = results
        self.render("test.html", title="My Clock", items=items, calenderlist = calenderlist )

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(8080)
    tornado.ioloop.IOLoop.current().start()

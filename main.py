import tornado.ioloop
import tornado.web
import motor.motor_tornado
import config
from datetime import datetime
client = motor.motor_tornado.MotorClient(config.DB_CONNECTION_STRING)
db = client.one_fx


class TestReadArticle(tornado.web.RequestHandler):
    async def get(self):
        articles = db.articles
        async for article in articles.find():
            self.write(
                "{created_at} - {header} - {body}<br>".format(**article))
        self.finish()


class TestWriteArticle(tornado.web.RequestHandler):
    async def get(self):
        document = {
            'created_at': datetime.now(),
            'header': 'first topic',
            'body': 'here will be the awesome text',
        }
        articles = db.articles
        await articles.insert(document)
        self.write("put to db finished")
        self.finish()

if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/test_write_article", TestWriteArticle),
        (r"/test_read_article", TestReadArticle),
    ], autoreload=True)
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()

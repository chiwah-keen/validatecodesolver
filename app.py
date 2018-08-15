#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import sys
import socket
from tornado import httpserver, ioloop
from tornado import web
from conf import config
from log import Log
socket.setdefaulttimeout(0.3)
reload(sys)
sys.setdefaultencoding('utf-8')


routes = [(r"/unoconv/pdf",   "handlers.messages.MessagesHandler"),
          ]


class Application(web.Application):
    def __init__(self):
        web.Application.__init__(self, routes, **config.settings)
        # self.redisdb = redis.StrictRedis(host=config.REDIS_HOST_TEST, port=config.REDIS_PORT,
        #                                  db=config.REDIS_DB_NUM, password=config.REDIS_PSWD)
        # self.mysqldb = torndb.Connection(host=config.MYSQL_SERVER, user=config.MYSQL_USER, port=config.MYSQL_PORT,
        #                                  password=config.MYSQL_PASSWORD, database=config.MYSQL_DB_MESSAGE,
        #                                  time_zone='+8:00', max_idle_time=252)
        self.log = Log("./logs/", name='bfbq', dividelevel=0, loglevel='info')


def start():
    application = Application()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(config.LISTEN_PORT)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    start()
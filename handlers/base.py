#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import time, logging, json, traceback
from tornado import web, gen


class BaseHandler(web.RequestHandler):
    @property
    def mysqldb(self):
        return self.application.mysqldb

    @property
    def redisdb(self):
        return self.application.redisdb

    @property
    def log(self):
        return self.application.log

    def prepare(self):
        self.ret = {'status': 0, 'request_id': str(int(time.time() * 1000000)), 'message': ''}
        logging.info(self.ret)

    def send_json(self, jsonobj):
        self.write(jsonobj)

    def get_json(self):
        try:
            return json.loads(self.request.body)
        except Exception as e:
            logging.error(traceback.format_exc())
            return None

    def send_status_message(self, status, messages):
        self.ret['status'] = status
        self.ret['message'] = messages
        self.send_json(self.ret)

    def send_data(self, data):
        self.ret['data'] = data
        self.send_json(self.ret)

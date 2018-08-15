#! /usr/bin/env python
# coding: utf-8
# author:zhihua

import traceback
from base import BaseHandler


class CaptchaValidateHandler(BaseHandler):

    def post(self):
        try:
            
        except Exception as e:
            self.log.error(traceback.format_exc())
            self.send_status_message(-1, traceback.format_exc())

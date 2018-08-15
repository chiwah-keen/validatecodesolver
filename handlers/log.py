#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
该类将不同级别的日志文件输入到不同的文件
'''

import os
import logging
import logging.handlers
from logging.handlers import RotatingFileHandler


class Log(object):
    LOG_LEVELS = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING, "error": logging.ERROR}

    def __init__(self,  path, name="", loglevel="", maxsize=500 * 1024 * 1024, fmt=None, backupcount=5, dividelevel=0):
        self.log_prefix = name or "dg"
        self.log_path = path or "/tmp/tnlog/"
        self.log_maxsize = maxsize
        self.log_level = self.LOG_LEVELS.get(loglevel.lower()) or logging.DEBUG
        self.log_backupcount = backupcount
        self.log_fmt = fmt or "[%(levelname)s] %(asctime)s-%(filename)s:%(lineno)s %(message)s"
        self._logger = dict()
        self.divid_levl = dividelevel
        if self.divid_levl == 0:
            self.init_logger0()
        elif self.divid_levl == 1:
            self.init_logger1()
        elif self.divid_levl == 2:
            self.init_logger2()
        else:
            raise Exception("The Divide Level not supported.")

    def init_logger(self, log_file, lev=None):
        handler = RotatingFileHandler(log_file, maxBytes=self.log_maxsize,
                                      backupCount=self.log_backupcount)
        formatter = logging.Formatter(self.log_fmt)
        handler.setFormatter(formatter)
        self.logger[self.logfd(lev)] = logging.getLogger(lev)
        self.logger[self.logfd(lev)].addHandler(handler)
        self.logger[self.logfd(lev)].setLevel(self.log_level)

    def init_logger0(self):
        log_file = os.path.join(self.log_path, "%s-%s.log" % (self.log_prefix, "log"))
        self.init_logger(log_file)

    def init_logger1(self):
        for lev, _ in self.LOG_LEVELS.items():
            log_file = os.path.join(self.log_path, "%s-%s.log" % (self.log_prefix, lev))
            self.init_logger(log_file, lev)

    def init_logger2(self):
        for lev, _ in self.LOG_LEVELS.items():
            log_path = os.path.join(self.log_path, lev)
            if not os.path.isdir(log_path):
                os.mkdir(log_path)
            log_file = os.path.join(log_path, "%s-%s.log" % (self.log_prefix, lev))
            self.init_logger(log_file, lev)

    @property
    def logger(self):
        return self._logger

    def logfd(self, lev):
        return 'log' if self.divid_levl == 0 or lev is None else lev

    def debug(self, m):
        return self.logger[self.logfd('debug')].debug(m)

    def DEBUG(self, m):
        return self.debug(m)

    def info(self, m):
        return self.logger[self.logfd('info')].info(m)

    def INFO(self, m):
        return self.info(m)

    def warn(self, m):
        return self.logger[self.logfd('warning')].warn(m)

    def WARN(self, m):
        return self.warn(m)

    def warning(self, m):
        return self.warn(m)

    def WARNING(self, m):
        return self.warn(m)

    def error(self, m, exc_info=True):
        return self.logger[self.logfd('error')].error(m, exc_info=exc_info)

    def ERROR(self, m):
        return self.error(m, exc_info=True)

if __name__ == "__main__":
    l = Log("./", dividelevel=2, loglevel="debug")
    l.debug("abcde")
    l.info("abcde")
    l.warn("abcde")
    try:
        raise Exception("my .... test")
    except:
        l.error("abcde")

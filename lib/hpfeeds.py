# WARNING: code not tested
# CODE BASE: https://raw.githubusercontent.com/mushorg/conpot/master/conpot/core/loggers/hpfriends.py

import socket
import hpfeeds
import gevent
import logging

logger = logging.getLogger(__name__)


class HPFeeds(object):

    def __init__(self, host, port, ident, secret, channels, max_retries=5):

        print "WARNING: This code was not tested"  # FIXME

        self.host = host
        self.port = port
        self.ident = ident
        self.secret = secret
        self.channels = channels
        self.max_retries = max_retries
        self.__initial_connection = False

    def connect(self):
        self.greenlet = gevent.spawn(self.__connect, self.host, self.port, self.ident, self.secret)

    def __connect(self, host, port, ident, secret):
        self.connection = hpfeeds.new(host, port, ident, secret)
        self.__initial_connection = True

    def wait(self):
        gevent.sleep(1)

    def send(self, event):
        retries = 0

        if not self.__initial_connection:
            error_msg = 'Connection to hpfeeds not established yet.'
            logger.warning(error_msg)
            return False

        else:
            while True:
                if retries >= self.max_retries:
                    break

                try:
                    self.connection.publish(self.channels, event)
                    return True

                except socket.error:
                    self.connect()
                    self.wait()
                    retries += 1

            error_msg = self.connection.wait()
            logger.warning(error_msg)
            return False

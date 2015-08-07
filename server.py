# -*- coding: utf-8 -*-

import zerorpc


class Interface(object):
    def ping(self):
        print 'server been called.'
        return 'ping'

if __name__ == '__main__':
    s = zerorpc.Server(Interface(), heartbeat=None)
    s.bind('tcp://*:7766')
    s.run()

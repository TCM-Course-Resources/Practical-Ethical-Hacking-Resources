#!/usr/bin/env python

import sockets

host = '127.0.0.1'
port = 4445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(host,port)

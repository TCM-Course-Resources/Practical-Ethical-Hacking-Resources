#!/usr/bin/env python

import socket

host = '127.0.0.1'
port = 4445

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

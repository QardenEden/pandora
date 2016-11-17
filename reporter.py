from datetime import datetime
from threading import Thread
from queue import Queue
from time import sleep
from sys import stdout

class Counter(Queue):
	def __init__(self):
		Queue.__init__(self)
		super().put(0)

	def put(self,item):
		while not self.empty(): self.get()
		super().put(item,False)

class Reporter(Thread):
	CREATE=0x101
	REGEN=0x010

	def __init__(self,queue,total,message):
		Thread.__init__(self)
		self.daemon=True

		self.message=message
		self.queue=queue
		self.total=total

	def run(self):
		loading=list('...     ')
		current=self.queue.get()
		time=str(datetime.now()).split('.')[0]

		while current<self.total-1:
			if not self.queue.empty(): current=self.queue.get()

			if self.message==0x101:
				stdout.write("\r[%s] [%s] creating socket %-*d/%d"%(time,''.join(loading),len(repr(self.total)),current+1,self.total))
			elif self.message==0x010:
				stdout.write("\r[%s] [%s] recreating socket %-*d/%d"%(time,''.join(loading),len(repr(lsocks)),current+1,lsocks))

			loading.insert(0,loading.pop())
			sleep(0.075)

		if self.message==0x101:
			print("\r[%s] [  DONE  ] creating socket %-*d/%d"%(time,len(repr(self.total)),current+1,self.total))
		elif self.message==0x010:
			print("\r[%s] [  DONE  ] recreating socket %-*d/%d"%(time,len(repr(lsocks)),current+1,lsocks))
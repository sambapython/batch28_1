import socket
try:
	s=socket.socket()
	host="www.google.com"
	port=8888#443#80
	s.connect((host,port))
	print "connected successfully!!!"
except Exception as err:
	print err
finally:
	s.close()
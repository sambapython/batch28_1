import socket
try:
	s=socket.socket()
	host = "tcloudost-VirtualBox"
	port=8889
	s.bind((host,port))
	s.listen(6)
	print "waiting for the client request"
	co, ci = s.accept()
	co.send("connected successfully!!!!!!")
except Exception as err:
	print err
finally:
	s.close()
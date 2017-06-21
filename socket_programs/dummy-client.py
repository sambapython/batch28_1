import socket
try:
	s=socket.socket()
	host = "tcloudost-VirtualBox"
	port=8889
	s.connect((host,port))
	ack = s.recv(1024)
	print "Ack: ", ack
except Exception as err:
	print err
finally:
	s.close()
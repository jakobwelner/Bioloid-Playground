#Based on Example: http://kmkeen.com/socketserver/

import socket
#import maya_handle
#import lib_general

def client(val, PORT = 6001, HOST = "localhost"):
    try:
	# SOCK_STREAM == a TCP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#sock.setblocking(0)  # optional non-blocking
	sock.connect((HOST, PORT))
	
	sock.send(val)
	reply = sock.recv(1024)  # limit reply to 16K
	
	sock.close()
	
	return reply
        #dataObj = lib_general.string_to_obj(reply)

        #maya_handle.set_ref_chain(dataObj)

    except:
	print "caught exception while trying to connect to server. Is it running?"
        raise


def dataToString(tId, tAng, tAngvel):
    dataString = {}

    for i, ang, angvel in zip(tId, tAng, tAngvel):
        dataString[i] = {"ang": ang, "angvel": angvel}
#    print "### DataToString >> repr obj: ", repr(dataString)
    client( repr(dataString) )





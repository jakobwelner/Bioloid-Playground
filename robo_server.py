from multiprocessing import Process, Queue
import maya_handle;reload(maya_handle)
import time
import os

queue = Queue()
FPS = 25


class Main():
	# servo loop
	def __init__(self):
		while 1:
			if queue.qsize():
				print 'Size:\t' + str(queue.qsize())
				print 'Value:\t' + str(queue.get())
			
			joints = maya_handle.getJointRotations()
			
			dataObj = {}
			for name, val in zip(["ref3.rotateY", "ref4.rotateY", "ref2.rotateY"], joints):
				dataObj[name] = val
				
			maya_handle.setJointRotations(dataObj)
			
			print joints
			time.sleep(1.0 / FPS)


def start_main():
	try:
		m = Main()
	except KeyboardInterrupt:
		print "start_main: exiting by keyboardinterrupt"


def start_server():
	try:
		#producer_process = Process(target=start_producer)
		consumer_process = Process(target=start_main)
	
		#producer_process.start()
		consumer_process.start()
		
		#producer_process.join()
		#consumer_process.join()
		
	except KeyboardInterrupt:
		print "start_server: exiting by keyboardinterrupt"
		
		
	
	
def initiate():
	# add maya pythonpath for tool-files, import files in Maya
	client_tcp.client("getAttr joint3.rotateY")
	
	
	#scriptPath = os.path.dirname( os.path.realpath(__file__) )
	#print scriptPath
	#client_tcp.client("import sys; sys.path.append('" + scriptPath + "')")
	#client_tcp.client("import maya_handle")
	#client_tcp.client("print maya_handle.joint_extension")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
#################################
	
	
class Producer():
	# socket server
	def __init__(self):
		for i in range(1,200):
			queue.put(i)


def start_producer():
	try:
		p = Producer()
	except KeyboardInterrupt:
		print "start_producer: exiting by keyboardinterrupt"



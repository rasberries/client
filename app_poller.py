import requests
import time
from threading import Thread
from cpu_info import *

class AppPoller:
	cpu_info = CpuInfo()
	stop_polling = False
	
	def __init__(self, base_url, endpoint = "/apps", timeout = 5):
		self.base_url = base_url
		self.endpoint = endpoint
		self.timeout = timeout
		self.serial_id = self.cpu_info.get_serial()
	
	def start(self):
		thread = Thread(target = self.poll_thread)
		thread.start()

	def poll_thread(self):
		full_url = self.base_url + self.endpoint + "/" + self.serial_id
		while not self.stop_polling:
			r = requests.get(full_url).json()
			if len(r) > 0:
				print "We found apps"
				time.sleep(self.timeout)
			else:
				print "Sleeping"
				time.sleep(self.timeout)
		
	def stop(self):
		self. stop_polling = True

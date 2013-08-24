
import config as conf
from cpu_info import *
import time
from threading import Thread
import requests
import signal


class AppPoller:
	cpu_info = CpuInfo()
	stop_polling = False
	
	def __init__(self, endpoint = "/values", timeout = 2):
		self.base_url = conf.base_url()
		self.endpoint = endpoint
		self.timeout = timeout
		self.serial_id = self.cpu_info.get_serial()
		def handler(signum, frame):
                        self.stop_polling = True
                signal.signal(signal.SIGINT, handler)
	
	def start(self):
		thread = Thread(target = self.poll_thread)
		thread.start()

	def poll_thread(self):
		full_url = self.base_url + self.endpoint + "/" + self.serial_id
		while not self.stop_polling:
			try:
				r = requests.get(full_url)
				if r.status_code < 300:
					apps = r.json()
					if len(apps) > 0: 
						#print apps
						print "We found apps"
				else:
					print full_url
					print "Error code %d" % r.status_code
			except Exception as e:
				print e
				print full_url
			finally:
				print "Sleeping"
				time.sleep(self.timeout)
		
	def stop(self):
		self. stop_polling = True

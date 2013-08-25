
from app_manager import *
import config as conf
from cpu_info import *
import time
from threading import Thread
import requests
import signal


class AppPoller:
	cpu_info = CpuInfo()
	stop_polling = False
	
	def __init__(self, endpoint = "devices", timeout = 2):
		self.base_url = conf.base_url()
		self.endpoint = endpoint
		self.timeout = timeout
		self.serial_id = self.cpu_info.get_serial()
		self.full_url = "%s/%s/%s/apps" % (self.base_url, self.endpoint, self.serial_id)
		def handler(signum, frame):
                        self.stop_polling = True
                signal.signal(signal.SIGINT, handler)
	
	def start(self):
		thread = Thread(target = self.poll_thread)
		thread.start()

	def poll_thread(self):
		while not self.stop_polling:
			try:
				r = requests.get(self.full_url)
				#print self.full_url
				if r.status_code < 300:
					apps = r.json()
					if len(apps) > 0:						
						for app in apps:
							#print app
							if len (app["app_stack"]) > 0 :
								for app_id in app["app_stack"]:
									app_manager = AppManager(app_id)
									app_manager.install()
				else:
					print "App Poller fail when  %s" % self.full_url
			except Exception as e:
				print "App Poller fail when  %s" % self.full_url
			finally:
				print "Sleeping"
				time.sleep(self.timeout)
		
	def stop(self):
		self. stop_polling = True

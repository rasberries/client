import requests
import time
import system
class AppPoller:
	def __init__(self, base_url, endpoint = "/apps", timeout = 1):
		self.base_url = base_url
		self.endpoint = endpoint
		self.timeout = timeout
	def poll(self):
		while True:
			r = requests.get(self.base_url + self.endpoint).json()
			if len(r) > 0:
				print "We found apps"
			else:
				print "Sleeping"
				time.sleep(self.timeout)
		


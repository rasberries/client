import requests 
import config as conf

class AppManager:
	
	def __init__(self, app_id, endpoint = "apps", ):
		self.base_url = conf.base_url()
		self.app_id = app_id
		self.endpoint = endpoint
		self.full_url = "%s/%s/%s" % (self.base_url, self.endpoint, self.app_id)
	
	def get(self):
		try:
			r = requests.get(self.full_url)
                        if r.status_code < 300:
                        	 apps = r.json()
                                 if len(apps) > 0:
					 print apps
                                         print "We found apps"
                        else:
                                 print self.full_url
                                 print "Error code %d" % r.status_code
                except Exception as e:
			print e
                        print self.full_url
	def install(self):
		self.get()
		self.download_dependencies()
		self.execute_dependency()
		self.update()

	def download_dependencies(self):
		pass

	def execute_dependency(self):
		pass

	def update(self):
		pass

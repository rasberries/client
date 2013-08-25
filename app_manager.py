import requests 
import config as conf
import subprocess

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
                        	 app = r.json()
				 print app
                        else:
                                 print "Error code %d" % r.status_code
                except Exception as e:
                        print self.full_url
	
	def install(self):
		try:
			app_info = self.get()
			for dep in app_info["dependencies"]:
				self.install_dependency(dep)
		except Exception as e:
			print "Failed to install app %s"  % e  
		self.update()

	def download_dependencies(self):
		pass

	def install_dependency(self, dep):
		bash_command = "apt-get install %s" % dep.name
                process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
                output = process.communicate()[0]
                print output


	def update(self):
		pass

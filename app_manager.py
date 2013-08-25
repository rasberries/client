import requests 
import config as conf
import random
import os
import subprocess
import urllib2

class AppManager:
	
	def __init__(self, app_id, endpoint = "apps", ):
		self.base_url = conf.base_url()
		self.base_path = conf.base_path() 
		self.app_id = app_id
		self.endpoint = endpoint
		self.full_url = "%s/%s/%s" % (self.base_url, self.endpoint, self.app_id)
	
	def get(self):
		try:
			r = requests.get(self.full_url)
                        if r.status_code < 300:
                        	 app = r.json()
				 print app
				 return app
                        else:
                                 print "Error code %d" % r.status_code
                except Exception as e:
                        print self.full_url
	
	def install(self):
		try:
			app_info = self.get()
			for dep in app_info["stubs"]:
				self.install_dependency(dep)
		except Exception as e:
			print "Failed to install app %s"  % e  
		self.update()

	def download_dependency(self, dep_url):
		dep_folder = "%s/rasp-%s" %(self.base_path , random.randint(999,9999) )
		os.makedirs(dep_folder)
		dep_file = dep_url.split('/')[-1]
		dep_path = "%s/%s" % (dep_folder, dep_file)
		self.download_file(dep_url, dep_path)	
		return dep_path

	def install_dependency(self, dep):
		dep_path = self.download_dependency(dep["url"])
		bash_command = "file %s" % dep_path
                process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
                output = process.communicate()[0]
                print output


	def update(self):
		"devices/move_app"
		{
				uuid :"",
				app_id:""
		}

	def download_file(self, url, path):
		dep_file = urllib2.urlopen(url)
		output = open(path,'wb')
		output.write(dep_file.read())
		output.close()

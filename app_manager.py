from cpu_info import *
import requests
import config as conf
import json
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
				 #print app
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
		self.update(app_info['id'])

	def download_dependency(self, dep_url):
		dep_folder = "%s/rasp-%s" %(self.base_path , random.randint(999,9999) )
		os.makedirs(dep_folder)
		dep_file = dep_url.split('/')[-1]
		dep_path = "%s/%s" % (dep_folder, dep_file)
		self.download_file(dep_url, dep_path)
		return dep_path

	def install_dependency(self, dep):
		dep_path = self.download_dependency(dep["url"])
		for cmd in dep["instructions"]:
			cmd_txt = cmd["command"]
			bash_command = "%s %s" % (cmd_txt, dep_path)
			print bash_command
                	process = subprocess.Popen(bash_command.split(), stdout=subprocess.PIPE)
                	output = process.communicate()[0]
                	print output

	def update(self, app_id, update_endpoint = "devices/move_app" ):
		update_url = "%s/%s" % (self.base_url,update_endpoint)
		uuid = CpuInfo().get_serial()
		update_data = {
				'uuid' : uuid,
				'app_id' : app_id
				}
		update_data_json = json.JSONEncoder().encode(update_data);
		#update_data = '{"uuid" : "000000001b34f454","app_id" : "sabinmarcu@gmail.com$NPM"}'
		#print update_data_json
		r = requests.put(update_url, data = update_data_json, headers = {'Content-Type': 'application/json'})
		if r.status_code <300:
			pass
			#dep = r.json()

	def download_file(self, url, path):
		dep_file = urllib2.urlopen(url)
		output = open(path,'wb')
		output.write(dep_file.read())
		output.close()

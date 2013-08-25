import configparser

config = configparser.ConfigParser()
config.read("/root/python-client/client/config/config.ini")

def base_url():
	return  config["DEFAULT"]["base_url"]

def base_path():
	return  config["DEFAULT"]["base_path"]

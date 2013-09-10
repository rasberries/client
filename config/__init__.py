import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.dirname(os.path.realpath(__file__)) + "/config.ini")

def base_url():
	return  config["DEFAULT"]["base_url"]

def base_path():
	return  config["DEFAULT"]["base_path"]

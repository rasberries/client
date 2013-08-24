import time
from app_poller import *

url = "http://10.0.0.238:56653/api"
endpoint = "/values"
app_poller = AppPoller(url, endpoint)
app_poller.start()
time.sleep(10)
app_poller.stop()


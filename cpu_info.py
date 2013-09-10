import sys, subprocess
class CpuInfo:
	def __init__(self):
		pass

	def get_serial(self):
		if sys.platform == "darwin": return self.get_serial_mac()
		else: return self.get_serial_linux()

	def get_serial_mac(self):
		serial = ""
		p = subprocess.Popen(["ioreg", "-rd1", "-c", "IOPlatformExpertDevice"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		f = out.split('\n')
		for line in f:
			if "IOPlatformUUID" in line:
				serial = line.replace("IOPlatformUUID","").replace("=","").replace("\"", "").strip()
		return serial

	def get_serial_linux(self):
		serial = ""
		cpu_info_file = "/proc/cpuinfo"
		f = open(cpu_info_file, "r")
		for line in f:
			if "Serial" in line:
				serial = line.replace("Serial","").replace(":","").strip()
		f.close()
		return serial


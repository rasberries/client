class CpuInfo:
	cpu_info_file = "/proc/cpuinfo"
	def __init__(self):
		pass
	def get_serial(self):
		serial = ""
		f = open(self.cpu_info_file, "r")
		for line in f:
			if "Serial" in line:
				serial = line.replace("Serial","").replace(":","").strip()
		f.close()
		return serial


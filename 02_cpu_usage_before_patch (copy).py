import psutil

def check_cpuusage(percent):
	usage = psutil.cpu_percent()
	return usage < percent

if not_check_cpu_usage(75):
	print("ERROR! CPU is overloaded")
else:
	print("Everything ok")
	

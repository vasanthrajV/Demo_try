import re
def rearrange_name(name):
	result = re.search(r"^([\w .-]*), ([\w .-]*)$",name)
	print('the change')	
	if result==None:
		return result
	return "{} {}".format(result[2], result[1])

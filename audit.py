
# Audit Pincodes
# pincode must be of 6 digits
# it should only contain numbers
# No wite space berween the postal code digits is allowed

def audit_post(pc):
	if pc.isdigit() and len(pc)==6:
		return pc
	elif len(pc)==7 and " " in pc:
		pc=pc.replace(" ","")
		if pc.isdigit():
			return pc
	else:
		return None

def audit_name(name):
	import re
	if "(" in name:
		return re.sub(r'\([^()]*\)', '', name).strip()
	elif "\\" in name:
		temp = re.sub(r'\\'," ",name)
		return re.sub(r'\s+',' ',temp)
	else:
		return name
import json
def ListToJson(outlist,filename):
	f=open(filename,"w")
	json.dump(outlist, f, sort_keys=True, indent=4)
	print(filename)


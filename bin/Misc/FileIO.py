import json

def ListToJson(outlist,filename):
	f=open(filename,"w")
	json.dump(outlist, f, sort_keys=True, indent=4)

def LoadJson(filename):
	f=open(filename,"r")
	root=json.load(f)
	return root


def DictToJson(outdict,filename):
	f=open(filename,"w")
	json.dump(outdict, f, indent=4)

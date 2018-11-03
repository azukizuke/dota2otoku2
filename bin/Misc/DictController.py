def addMultiDict(ddict,val1,val2):
	if val1 not in ddict:
		ddict[val1] = ({ val2 : 1})
	else:
		if val2 not in ddict[val1]:
			ddict[val1].update({ val2 : 1})
		else:
			ddict[val1][val2] += 1
			#ddict[val1].update({val2 : ddict[val1][val2] + 1})
	return ddict

def extendMultiDict(dict1,key1,dict2,key2):
	if key1 not in dict1:
		dict1.update({key1 : dict1[key2]})
	else:
		#dict1 for hero
		for heroid in dict1[key2]:
			if heroid not in dict1[key1]:
				print("---------------------------")
				print(key1)
				print(key2)
				print(heroid)
				print(dict1)
				dict1[key1].update({heroid : dict1[key2][heroid]})
				print(dict1)
				print("---------------------------")
			else:	
				#dict1[key1][heroid] += dict1[key2][heroid]
				dict1[key1].update({heroid : dict1[key2][heroid] + 1})
	return dict1

#import urlLoad
#import fileOut
#import const
def MakeMatchIDList(leagueid,leaguename,startid,endid):
#	matchIDList = []
#	print("make file" + str(leagueid))
#
#	num_rootin=0
#	while True:
#		if num_rootin==0:
#			url=urlLoad.makeMatchHistroyUrl(leagueid,const.APIKEY,const.MAXNUM,startid)
#			num_rootin=1
#		else:
#			url=urlLoad.makeMatchHistroyUrlNext(leagueid,const.APIKEY,const.MAXNUM,appendid)
#			
#		print("request league url : " + url)
#		root = urlLoad.convertJson(const.TIMEOUT,url)
#		result = root["result"]
#		matches = result["matches"]
#
#		for match in matches:
#			#list
#			if startid <= match["match_id"] :
#				if match["match_id"] <= endid:
#					if match not in matchIDList:
#			 			matchIDList.append(match["match_id"]);
#
#		appendid=matchIDList[-1]
#		print(appendid)
#		if len(matches) <= 1:
#			break
#
#	fileOut.outputMatchList(leaguename,matchIDList)


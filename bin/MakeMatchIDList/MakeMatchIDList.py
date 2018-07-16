import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Misc')
import UrlLoad
import json
#import fileOut
#import const

def MakeMatchIDList(leagueid,leaguename,api_key,startid,endid):
	matchIDList = []
	matchIDjson = {}
	print("make Match ID List json : " + str(leagueid))

	num_rootin=0
	appendid=0

	URL_TIMEOUT=300
	while True:

		##### Make Url #####
		url=MakeSteamMatchHistoryUrl(leagueid,api_key,appendid,num_rootin)
		print("request league url : " + url)

		#### Get root API json #####
		root = UrlLoad.convertJson(URL_TIMEOUT,url)
		result = root["result"]
		matches = result["matches"]

		##### add checkrootin  #####
		prev_matchid_len=len(matchIDList)
		print(prev_matchid_len)
		matchIDList=MakeJsonFromMatches(matchIDList,matches,num_rootin,startid,endid)
		print(len(matchIDList))
		if prev_matchid_len == len(matchIDList):
			break
		appendid=matchIDList[-1]
		num_rootin += 1

	print(json.dumps(matchIDList, sort_keys=True,indent=4))

def MakeSteamMatchHistoryUrl(leagueid,api_key,startid,add_flag):
	if add_flag < 1:
		apiurl="http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?league_id="+str(leagueid)+"&key=" + str(api_key)
	else:
		apiurl="http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1?league_id="+str(leagueid)+"&key=" + str(api_key) + "&start_at_match_id=" + str(startid)
		
	
	return apiurl

def MakeJsonFromMatches(matchIDList,matches,add_flag,startid,endid):
	add_count = 0
	for match in matches:
		if startid <= match["match_id"] :
			if match["match_id"] <= endid:
				if match["match_id"] not in matchIDList:
 					matchIDList.append(match["match_id"]);
	return matchIDList

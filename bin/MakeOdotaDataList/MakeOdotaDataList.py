import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Misc')
import UrlLoad
import json
#import fileOut
#import const

def MakeOdotaDataList(matchIDList):
	URL_TIMEOUT=300
	odotaDataDict={}

	for match_id in matchIDList:

		##### get url #####
		url=MakeOdotaAPIUrl(match_id)
		print("request odota api url : " + url)

		#### Get root API json #####
		root = UrlLoad.convertJson(URL_TIMEOUT,url)

		##### add Json dict  #####
		odotaDataDict[match_id] = root

	return odotaDataDict

def MakeOdotaAPIUrl(match_id):
	url="https://api.opendota.com/api/matches/" + str(match_id)
	return url


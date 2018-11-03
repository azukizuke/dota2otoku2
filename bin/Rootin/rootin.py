import sys
import os
import json

#####################init#################################
args=sys.argv

leagueid=int(args[1])
leaguename=args[2]
startid=int(args[3])
endid=int(args[4])
comp_leaguename=args[5]
leaguefilename=args[6]
BASEDIR=args[7]
steam_api_key=args[8]
odota_get_flag=int(args[9])

####################init after get BASEDIR ##############
sys.path.append(BASEDIR+"/MakeMatchIDList")
sys.path.append(BASEDIR+"/UrlLoad")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Misc')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../MakeOdotaDataList')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../MakeStat')
import MakeMatchIDList
import FileIO
import MakeOdotaDataList
import MakeLeagueStat

####################val#################################
matchIDList=[]
odotaDataList={}

filebase="../../data/" + str(leaguename)
try:
	os.mkdir(filebase)
except FileExistsError:
	pass

matchid_filename=filebase +"/"+ str(leaguename) + "_idlist.json"
odota_data_filename=filebase +"/"+ str(leaguename) + "_odotadatalist.json"
leaguestat_filename=filebase +"/"+ str(leaguename) + "_leaguestat.json"

####################json#################################

if not odota_get_flag == 0:
	##### get Matchlist json from league id #####
	matchIDList=MakeMatchIDList.MakeMatchIDList(leagueid,leaguename,steam_api_key,startid,endid)
	FileIO.ListToJson(matchIDList,matchid_filename)
	
	##### get Odota json from league id json #####
	matchIDListRoot=FileIO.LoadJson(matchid_filename)
	odotaDataList=MakeOdotaDataList.MakeOdotaDataList(matchIDListRoot)
	FileIO.DictToJson(odotaDataList,odota_data_filename)

##### analysis #####
odotaDataDictRoot=FileIO.LoadJson(odota_data_filename)

# League Stat analysis
leaguestatJson=MakeLeagueStat.MakeLeagueStat(odotaDataDictRoot)
FileIO.DictToJson(leaguestatJson,leaguestat_filename)
# Hero Stat anaysis
#

##### output dokuwiki #####

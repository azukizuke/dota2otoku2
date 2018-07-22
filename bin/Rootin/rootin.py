import sys
import os

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

####################init after get BASEDIR ##############
sys.path.append(BASEDIR+"/MakeMatchIDList")
sys.path.append(BASEDIR+"/UrlLoad")
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Misc')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../MakeOdotaDataList')
import MakeMatchIDList
import FileIO
import MakeOdotaDataList

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
##### get Matchlist json from league id #####
matchIDList=MakeMatchIDList.MakeMatchIDList(leagueid,leaguename,steam_api_key,startid,endid)
FileIO.ListToJson(matchIDList,matchid_filename)

##### get Odota json from league id json #####
matchIDListRoot=FileIO.LoadJson(matchid_filename)
odotaDataList=MakeOdotaDataList.MakeOdotaDataList(matchIDListRoot)
FileIO.DictToJson(odotaDataList,odota_data_filename)

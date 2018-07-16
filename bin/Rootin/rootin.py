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
import MakeMatchIDList
import FileIO

####################val#################################
matchIDList=[]

filebase="../../data/" + str(leaguename)
try:
	os.mkdir(filebase)
except FileExistsError:
	pass

matchid_filename=filebase +"/"+ str(leaguename) + "_idlist.json"
##### get Matchlist json from league id #####
matchIDList=MakeMatchIDList.MakeMatchIDList(leagueid,leaguename,steam_api_key,startid,endid)
FileIO.ListToJson(matchIDList,matchid_filename)



















#fileOut.initMakeFolder(leaguename)
#
##Get MatchIdList
#if leagueid != 0:
#	MakeMatchList.makeMatchIdListFile(leagueid,leaguename,startid,endid)
#
##Get MatchDataList
#MatchDataList=[]
#MatchDataList=CalcMatchDataList.getMatchDataList(leaguename)
#
####Heroes List Class Init
#heroesStatistics = HeroesStatistics.HeroesStatistics()
#heroesStatistics.initHeroList()
#
#for MatchData in MatchDataList:
#	#MatchData内にあるplyersdata
#	heroesStatistics.addHeroesMatchPlayerJson(MatchData["players"])
#	#pickban data keisan
#	heroesStatistics.addHeroesMatchPickBan(MatchData)
#
########HeroStat Calc
#heroesStatistics.calcHeroesStatistics()
#
########Output Calc
#heroesStatistics.outHeroesStatistics(leaguename)

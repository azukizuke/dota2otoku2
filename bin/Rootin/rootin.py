import sys

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
import MakeMatchIDList

##### get Matchlist json from league id #####
MakeMatchIDList.MakeMatchIDList(leagueid,leaguename,steam_api_key,startid,endid)


















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

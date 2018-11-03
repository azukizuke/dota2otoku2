import sys,os
import copy
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../Misc')
import UrlLoad
import json
import DictController
import FileIO
import DictController

def MakeLeagueStat(root):
	leaguestatJson={}
	leaguestatJson.update({"pickban" : MakePickBan(root)})
	
	return(leaguestatJson)

def MakePickBan(root):
	pb_dict={}
	convert_json=FileIO.LoadJson(os.path.dirname(os.path.abspath(__file__)) + '/../../json/pickban_convert.json')

	for match_id in root:
		match_root=root[match_id]
		picks_bans=match_root["picks_bans"]

		##### 2 dimention add #####
		print(pb_dict)
		for pickban in picks_bans:
			DictController.addMultiDict(pb_dict,str(pickban["order"]),pickban["hero_id"])

	##### convert pickban order to String
	conv_pb_dict=MakePickBanConv(pb_dict,convert_json)
	return(conv_pb_dict)

def MakePickBanConv(pb_dict,conv_json):
	conv_pb_dict={}
	for convkey in conv_json:
		for order in conv_json[convkey]:
			if convkey not in conv_pb_dict:
				conv_pb_dict[convkey] = copy.copy(pb_dict[order])
			else :
				for heroid in pb_dict[order]:
					if heroid not in conv_pb_dict[convkey]:
						conv_pb_dict[convkey].update({heroid : pb_dict[order][heroid]})	
						pass
					else:
						conv_pb_dict[convkey][heroid] += 1
						pass
	return(conv_pb_dict)

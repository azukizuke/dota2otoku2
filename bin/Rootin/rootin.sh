#!/bin/bash

BASEDIR=~/dota2otoku2/bin

##### arg #####
leagueid=9870
leaguename=test_ti2018
#startid=3960615221
startid=3972835248
endid=9999999999
comp_leaguename=na
leaguefilename=na

APIKEY=`cat /var/dota2otoku2/steam_api.txt`

##### #####

python3 $BASEDIR/Rootin/rootin.py $leagueid $leaguename $startid $endid $comp_leaguename $leaguefilename $BASEDIR $APIKEY

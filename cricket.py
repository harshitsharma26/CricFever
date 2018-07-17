import requests
import re
from selectMatch import match_url
from bs4 import BeautifulSoup
import webbrowser
import time
import notify2
def sendmessage(message,team1,team2,score1,score2):
	notify2.init(data)
	score=team1+' '+score1+' vs '+team2+' '+score2
	n = notify2.Notification(score, message)
	notify2.URGENCY_NORMAL
	n.show()
	return



previousData="12"   # random initial data	
data="1"			# random initial data	
while True:	
	page_commentary = requests.get(match_url)
	html = BeautifulSoup(page_commentary.content, "html.parser")
	soup = html.find_all('div',{'class' : 'commentary-item'})
	#latest commentary
	description=soup[0].find("div",{"class":"description"})
	time_stamp=soup[0].find("div",{"class":"time-stamp"})
	commentary = ""
	fetchTeam = html.find_all('span',{'class':'cscore_name cscore_name--abbrev'})
	fetchScore = html.find_all('div',{'class':'cscore_score '})
	team1=fetchTeam[0].text
	team2=fetchTeam[1].text
	score1=fetchScore[0].text
	score2=fetchScore[1].text
	if time_stamp != None:
		commentary+=time_stamp.text
	commentary += " "
	if description != None:
		commentary+=(description.text)
	#print(commentary)
	previousData=data
	data=commentary
	#time.sleep(1)
	if previousData!=data:
		sendmessage(commentary,team1,team2,score1,score2)



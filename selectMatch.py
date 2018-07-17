import requests
import re
from bs4 import BeautifulSoup
import webbrowser
import time


url='http://www.espncricinfo.com/scores'
matches = requests.get(url)
html = BeautifulSoup(matches.content, "html.parser")
match = html.find_all('div',{'class' : 'cscore_link cscore_link--button'})
allMatches = []
cnt = 1
for cur_match in match:
	status=cur_match.find("span",{"class":"cscore_time"})
	if status != None:
		if status.text == 'LIVE':	
			match_url=cur_match.find("a")
			allMatches.append(match_url['href'])
			match_info = cur_match.find_all("span",{"class":"cscore_name cscore_name--long"})
			match_info2 = cur_match.find("span",{"class":"cscore_name cscore_name--abbrev"})
			print(str(cnt)+'.'+match_info[0].text+' vs '+match_info[1].text)
			cnt = cnt + 1 
if len(allMatches) == 0:
	print("Sorry, no matches available at this point of time") 
	quit()
print('Select the match you want to see')	
selected= int(input())
match_url= allMatches[selected-1]
			

			
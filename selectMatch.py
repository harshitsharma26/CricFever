import re
from bs4 import BeautifulSoup
import time
import urllib

url='http://www.espncricinfo.com/scores'
matches = urllib.request.urlopen(url)
html = BeautifulSoup(matches, "html.parser")
#print(html.prettify())
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
			#match_info2 = cur_match.find("span",{"class":"cscore_name cscore_name--abbrev"})
			print(str(cnt)+'.'+match_info[0].text+' vs '+match_info[1].text)
			cnt = cnt + 1 
if len(allMatches) == 0:
	print("Sorry, no matches available at this point of time") 
	quit()
print('Select the match you want to see')	
selected= int(input())

while selected>len(allMatches): 
	print("Invalid Input. Please Try Again")
	selected= int(input())
	
match_url= allMatches[selected-1]
			

			
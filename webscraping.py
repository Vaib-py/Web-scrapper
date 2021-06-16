
import requests #Helps in downloading Html file form sites
from bs4 import BeautifulSoup #used to scrap and clean up data
import pprint
res = requests.get('https://news.ycombinator.com/news') # Grabbing the data 

#Cleaning up the recieved Data

soup = BeautifulSoup(res.text,'html.parser') #Telling BS that this thing needs to be scraped 
links = soup.select('.storylink') #Getting all the links of our stories
subtext = soup.select('.subtext') #Getting all the Votes of diffrent stories

def sort_news_from_votes (hnlist):
    return sorted (hnlist,key = lambda k:k['votes'],reverse = True)



def custom_hn (links,subtext):  #Actual Cleaning process
    hn = []
    for idx,item in enumerate(links):
        title = links [idx].getText()
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99 :
                hn.append({'title':title,'link':href,'votes': points})
    return sort_news_from_votes (hn)
  
pprint.pprint(custom_hn(links, subtext)) 
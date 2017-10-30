#print "Ashish Kumar"
import requests
import pprint
import pymongo
from bs4 import BeautifulSoup


from pymongo import MongoClient
client = MongoClient('localhost',27017)

db = client['test-database']

collection = db['db-collection']

post ={
        "author": "Mike",
        "text": "My first blog post!"
    }

post_id = collection.insert_one(post).inserted_id

print post_id

pprint.pprint(collection.find_one())
url = 'http://www.espncricinfo.com/icc-champions-trophy-2013/engine/match/566948.html'

page = requests.get(url)

print page

soup = BeautifulSoup(page.content, 'html.parser')

#print soup

win_div = soup.find('div', class_ = 'score')

win_text = win_div.text

print win_text


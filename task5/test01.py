import urllib2
import json
import pymongo
from pymongo import MongoClient

client = MongoClient('localhost', 3306)
db = client['pymongo_test']
posts = db.posts

req = urllib2.Request("http://localhost:7000/api/v1.3/subcontainers/docker/adba6b90cd9b0ecbac4c35f0753ea02afd73f175c1309911aa7a4a718d87181e")
req2 = urllib2.Request("http://localhost:7000/api/v1.3/subcontainers/docker/adba6b90cd9b0ecbac4c35f0753ea02afd73f175c1309911aa7a4a718d87181e")
opener = urllib2.build_opener()
f = opener.open(req)
f1 = opener.open(req2)
json1 = json.loads(f.read())
json2 = json.loads(f1.read())

for i in range(len(json1[0]['stats'])):
    print json1[0]['stats'][i]['cpu']['usage']['total']
    print type(json1[0]['stats'][i]['cpu']['usage'])
    posts.insert_one(json1[0]['stats'][i]['cpu']['usage'])
    #posts.insert_one(json[0]['stats'][i]['cpu']['usage'])
    posts.insert_one(json2[0]['stats'][i]['cpu']['usage'])
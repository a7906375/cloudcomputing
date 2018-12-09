#import pymongo

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycol = mydb["customers"]

#mydict = { "name": "John", "address": "Highway 37" }

#x = mycol.insert_one(mydict)

#import requests
#r = requests.get('https://api.github.com/events')



#url='http://localhost:7000/api/v1.3/subcontainers/docker/66fc0d5709a3728b5563b02ee78dd693f78aac1ce4989a60bb3aa309ebcb66ea'

#response = requests.get(url)
#if response.status_code != 200:
    #print('Failed to get data:', response.status_code)
#else:
#    print('First 100 characters of data are')
#    print(response.text[:100]
#
#
import requests 
try:
    from pymongo import MongoClient
except ImportError:
    raise ImportError('PyMongo is not installed')


class MongoDB(object):
    def __init__(self, host='localhost', port=27017, database_name=None, collection_name=None):
        try:
            self._connection = MongoClient(host=host, port=port, maxPoolSize=200)
        except Exception as error:
            raise Exception(error)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._connection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]

    def insert(self, post):
        # add/append/new single record
        post_id = self._collection.insert_one(post).inserted_id
        return post_id


url = 'http://localhost:7000/api/v1.3/subcontainers/docker/66fc0d5709a3728b5563b02ee78dd693f78aac1ce4989a60bb3aa309ebcb66ea'
response = requests.get(url)
data = response.text
if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    print('First 100 characters of data are')
    print(data[:10000])

print('[*] Parsing response text')
data = data.split('\n')
data_list = list()
for value in data:
    if 'memory,cpu' not in value:
        if value:
            value = value.split(',')
            data_list.append({'memory': str(value[0]), 'cpu': str(value[1])})
            #data_list.append({'memory': int(value[0]), 'cpu': float(value[1])})

print(data_list)

#print('[*] Pushing data to MongoDB ')
#mongo_db = MongoDB(database_name='Climate_DB', collection_name='climate_data')

#for collection in data_list:
#    print('[!] Inserting - ', collection)
#    mongo_db.insert(collection)
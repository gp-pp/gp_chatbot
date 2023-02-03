import pymongo

def db_connection():
    url = "mongodb://harshxtanwar:db12345@ac-zdnook2-shard-00-00.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-01.dvbpycz.mongodb.net:27017,ac-zdnook2-shard-00-02.dvbpycz.mongodb.net:27017/?ssl=true&replicaSet=atlas-83le6q-shard-0&authSource=admin&retryWrites=true&w=majority"
    myclient = pymongo.MongoClient(url)
    mydb = myclient["gp_profiles"]
    mycol = mydb["user_chatbot"]

    return mycol

# data = []
# for x in mycol.find():
#   print(x)
#   data.append(x)

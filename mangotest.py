import pymongo
client = pymongo.MongoClient("mongodb+srv://soodtanishq27:<Soodtanishq1230>@cluster0.jihydkm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"tanishq",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "sood"
}

d = {
    "name":"tanishq",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "sood"
}

d = {
    "name":"tanishq",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "sood"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["mydatabase3"]

print("Available Databases: ",myclient.list_database_names())
mycol = mydb["customer"]

mydict = {'name':'John',"address":"Highway 37"}
x = mycol.insert_one(mydict)
print("\nInserted collection with random ID:",x.inserted_id)

mydict1 = {"_id":"Apple","name":"William","address":"SideWay 1633 "}

y=mycol.insert_one(mydict1)
print("\nCustom ID for Inserted collection:",y.inserted_id)

mylist = [{"_id":"1","name":"Amy","address":"Apple st 653"},
          {"_id":"2","name":"Hannah","address":"Mountain 21"},
          {"_id":"3","name":"Michel","address":"Valley 345"},
          {"_id":"4","name":"Sandy","address":"Ocean blue"},
          {"_id":"5","name":"Betty","address":"Green Grass"}]
z=mycol.insert_many(mylist)

print("\nAll the ID's of multiple collection insertion")
print(z.inserted_ids)
x=mycol.find_one("Apple")
print("\nFinding an collection based on ID of the collection: ",x)
print("\nPrinting entire data from collection")

for x in mycol.find():
    print(x)
    print("\n Printing only name value from collection")

for x in mycol.find({},{"_id":0,"name":1}):
    print(x)
import pymongo
from datetime import datetime

#connection2 = pymongo.MongoClient("mongodb://ale:ale123456@cluster0-yowax.mongodb.net")
#dbTest = connection2["test"]
#print(dbTest)
#dbTest.create_collection("Users")
#dbTest.create_collection("Messages")
#collUsers    = connection2["Users"]
#collMessages = connection2["Messages"]

connection1 = pymongo.MongoClient("mongodb://localhost:27017")
dbMessaging = connection1["Messaging"]
collUsers    = dbMessaging["Users"]
collMessages = dbMessaging["Messages"]

'''
collUsers.insert_one({"username"  : "hpiza", 
                      "name"      : "Iván Piza",
                      "password"  : "nopassword",
                      "email"     : "hpiza@iteso.mx",
                      "lastlogin" : datetime(2020, 5, 6),
                      "height"    : 1.75,
                      "weight"    : 78.5,
                      "age"       : 42
                     })
'''

# docFound = collUsers.find_one({"username" : "jperez"})  # SELECT 
# print("Name:", docFound["name"], " Email:", docFound["email"])
# print()

#query = {"username" : "mgomez"}
#values = { "$set" : {"weight" : 59.3, "age" : 24, "status" : "single"} }
#collUsers.update_one(query, values)

#query = {"username" : "hpiza"}
#collUsers.delete_one(query)

for docUser in collUsers.find():
    #print("Name:", docUser["name"], " Email:", docUser["email"])
    print(docUser)
    print("----------")

# dbMessaging.drop()   
#connection1.drop_database("Messaging")
'''
collMessages.insert_one({"from" : "ppalos", 
                         "to" : "jperez", 
                         "message" : "¡Hola Juan! acabo de salir de clase",
                         "when" : datetime(2020,5,7),
                         "status" : "received"
                         })
'''
for docMessage in collMessages.find({"to" : "ppalos", "status" : "viewed"},
                                    { "_id" : 0, "from" : 1, "message" : 1 }
                                    ):
    print(docMessage)

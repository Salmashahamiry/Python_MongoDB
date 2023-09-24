import pymongo

# Replace these values with your MongoDB server information
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["NewDB"]
collection = db["FirstCollection"]

# Insert a document
data_to_insert = {"name": "Bidar", "skill": "python", "skill2": "MongoDB"}
collection.insert_one(data_to_insert)
print("Document inserted successfully.")

# Retrieve documents
documents = collection.find()
print("Documents in the collection:")
for document in documents:
    print(document)

# Close the MongoDB connection
client.close()

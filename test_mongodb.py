
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Ankush0050:<Ankush0050>@cluster0.cingamw.mongodb.net/?retryWrites=true&w=majority&appName=cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
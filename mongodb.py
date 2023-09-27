from pymongo.mongo_client import MongoClient
import os
import dotenv

# cargamos las variables de entorno
dotenv.load_dotenv()

# leemos las varaibles de entorno
usuario = os.getenv('USR_MONGO')
passwd = os.getenv('PSW_MONGO')

uri = f"mongodb+srv://{usuario}:{passwd}@cluster0.lbxiwj7.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Conexión Correcta a MongoDB!")
except Exception as e:
    print(e)
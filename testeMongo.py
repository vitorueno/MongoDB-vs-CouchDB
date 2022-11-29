import pymongo

# criando conexão usando porta padrão do localhost
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# criando uma database
mydb = myclient["mydatabase"]

# criando uma collection (equivalente à tabela)
mycol = mydb["customers"]

# criando um dado
mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)

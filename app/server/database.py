import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = 'mongodb://localhost:27017'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.pessoas

pessoas_collection = database.get_collection('pessoas_collection')


# helpers


# processar os resultados do BD em um dicionário python
def pessoa_helper(pessoa) -> dict:
    return {
        'id': str(pessoa['_id']),
        'nome': pessoa['nome'],
        'endereco': pessoa['endereco'],
        'email': pessoa['email'],
        'idade': pessoa['idade'],
    }


# operações crud

# pegar todas as pessoas
async def retrieve_pessoas():
    pessoas = []
    async for pessoa in pessoas_collection.find():
        pessoas.append(pessoa_helper(pessoa))
    return pessoas


# adicionar pessoa
async def add_pessoa(pessoa_data: dict) -> dict:
    pessoa = await pessoas_collection.insert_one(pessoa_data)
    nova_pessoa = await pessoas_collection.find_one({"_id": pessoa.inserted_id})
    return pessoa_helper(nova_pessoa)


# pega a pessoa com o id
async def retrieve_pessoa(id: str) -> dict:
    pessoa = await pessoas_collection.find_one({"_id": ObjectId(id)})
    if pessoa:
        return pessoa_helper(pessoa)


# atualiza a pessoa com o id especificado
async def update_pessoa(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    pessoa = await pessoas_collection.find_one({"_id": ObjectId(id)})
    if pessoa:
        updated_pessoa = await pessoas_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_pessoa:
            return True
        return False


# exclui o estudante com o id específicado
async def delete_pessoa(id: str):
    pessoa = await pessoas_collection.find_one({"_id": ObjectId(id)})
    if pessoa:
        await pessoas_collection.delete_one({"_id": ObjectId(id)})
        return True

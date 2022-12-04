from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder


from server.database import (
    add_pessoa,
    delete_pessoa,
    retrieve_pessoa,
    retrieve_pessoas,
    update_pessoa,
    delete_pessoas
)

from server.models.pessoa import (
    ErrorResponseModel,
    ResponseModel,
    PessoaSchema,
    UpdatePessoaModel
)

router = APIRouter()


@router.post("/", response_description="Dados da pessoa adicionados com sucesso")
async def add_pessoa_data(pessoa: PessoaSchema = Body(...)):
    pessoa = jsonable_encoder(pessoa)
    new_pessoa = await add_pessoa(pessoa)
    return ResponseModel(new_pessoa, "pessoa adicionada com sucesso.")


@router.get("/", response_description="Pessoas recuperadas")
async def get_pessoas():
    pessoas = await retrieve_pessoas()
    if pessoas:
        return ResponseModel(pessoas, "Pessoas recuperadas com sucesso")
    return ResponseModel(pessoas, "Lista vazia retornada")


@router.get("/{id}", response_description="Pesssoa específica recuperada")
async def get_pessoa_data(id):
    pessoa = await retrieve_pessoa(id)
    if pessoa:
        return ResponseModel(pessoa, "Dados da pessoa recuperados com sucesso")
    return ErrorResponseModel("Erro: ", 404, "pessoa doesn't exist.")


# atualizar pessoa
@router.put("/{id}")
async def update_pessoa_data(id: str, req: UpdatePessoaModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_pessoa = await update_pessoa(id, req)
    if updated_pessoa:
        return ResponseModel(
            f"Pessoa com id: {id} atualizado com sucesso",
            "Pessoa atualizada com sucesso",
        )
    return ErrorResponseModel(
        "Erro: ",
        404,
        "Houve um erro ao atualizar a pessoa",
    )


# deletar pessoa
@router.delete("/{id}", response_description="Pessoa deletada do banco de dados")
async def delete_pessoa_data(id: str):
    deleted_pessoa = await delete_pessoa(id)
    if deleted_pessoa:
        return ResponseModel(
            f"Pessoa com id: {id} removida", "Pessoa removido com sucesso"
        )
    return ErrorResponseModel(
        "Erro: ", 404, f"pessoa {id} não existe"
    )


@router.delete("/", response_description="Pessoas deletadas do banco de dados")
async def delete_pessoas_data():
    deleted_pessoa = await delete_pessoas()
    if deleted_pessoa:
        return ResponseModel(
            f"Pessoas removidas com sucesso", "Pessoas removidas"
        )
    return ErrorResponseModel(
        "Erro: ", 404, f"erro ao remover pessoas"
    )

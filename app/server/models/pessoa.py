from typing import Optional

from pydantic import BaseModel, EmailStr, Field

# fastAPI usa o pydantic para criar as documentações com swagger UI (/docs)

# representação da pessoa no mongoDB


class PessoaSchema(BaseModel):
    # ... significa obrigatório (poderia ser None ou valor padrão)
    nome: str = Field(...)
    email: EmailStr = Field(...)
    endereco: str = Field(...)
    idade: int = Field(..., gt=0, lt=200)  # gt = greater than; lt = less than

    class Config:
        schema_extra = {
            'exemplo': {
                'nome': 'Vítor',
                'email': 'vitor@email.com',
                'endereco': 'rua bonita, 123 - Cidade, Estado, País',
                'idade': 20
            }
        }


class UpdatePessoaModel(BaseModel):
    nome: Optional[str]
    email: Optional[EmailStr]
    endereco: Optional[str]
    idade: Optional[int]

    class Config:
        schema_extra = {
            'exemplo': {
                'nome': 'Vítor',
                'email': 'vitor@bla.com',
                'endereco': 'rua bonita, 123 - Cidade, Estado, País',
                'idade': 20
            }
        }


def ResponseModel(data, message):
    return {
        'data': [data],
        'code': 200,
        'message': message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}

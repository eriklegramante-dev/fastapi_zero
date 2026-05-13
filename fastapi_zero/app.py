from fastapi import FastAPI
from http import HTTPStatus

from fastapi_zero.schemas import Message, UserSchema, UserPublic, UserDB

app = FastAPI()

database = []


@app.get(
    '/',
    status_code=HTTPStatus.OK,  # 200
    response_model=Message,
)
def read_root():
    return {'message': 'Olá, mundo!'}


@app.post(
    '/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic
)  # 201
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id

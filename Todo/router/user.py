from fastapi import APIRouter,Query
from .. import models,schema
from ..repository import todo
from typing import List

router=APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post('/')
def create(user: models.User):
   
    return todo.create(user)

@router.delete('/{id}')
def delete(id:int):
    
    return todo.delete(id)



@router.put('/{id}')
def update(id:int,user:models.User):

    return todo.update(id,user)

# @router.get('/',response_model=List[schema.User_Show])
# def show():
    
#     return todo.done()

@router.get('/',response_model=List[schema.User_Show])
async def showall():

    return todo.showall()


@router.get('/{value}')
def filter(value):
    return todo.filter(value)
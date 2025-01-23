
from ..database import blogs_collection
from fastapi import HTTPException,status,Query
from .. import models
from typing import List


def create(user):
    user=user.dict()
    result= blogs_collection.insert_one(user)
    return 'insert successfully'


def delete(id:int):
    result=blogs_collection.find_one_and_delete({"id": id})
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{id} not found')
    return 'Delete successfully'

def update(id,user):


    old={'id':id}
    new={'$set':user.dict()}
    result=blogs_collection.find_one_and_update(old,new)

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user name {id} is not found')
    
    return 'Successfully updated..'

# def filter(value):

#     userss=blogs_collection.find()
#     users=list(userss)
    
#     result=[]

#     for user in users:
#         result.append(user['title'])
#     l=[i for i in result if value in i ]    
    

#     return l

def filter(value):
    # Use a list comprehension to directly filter titles from the cursor
    result = [
        user['title']
        for user in blogs_collection.find({}, {"title": 1})
        if value.lower() in user['title'].lower()
    ]
    return result


   
    




# def show(title:str):
#     user=blogs_collection.find_one({'title':title})
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'{title} is not found in todo list')
#     # user["_id"] = str(user["_id"])

#     return user

# def done():
#     userss=blogs_collection.find()
#     users=list(userss)
    
#     done_item=[user for user in users if user['status']==False]
   

#     return done_item        

def showall():
    userss=blogs_collection.find()
    users=list(userss)
    
    return users

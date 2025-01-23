from pydantic import BaseModel

class Basee(BaseModel):    
    class Config():
        orm_mode=True  
class User_Show(Basee):
    id:int
    title:str
    status:bool
   
class Filter(BaseModel):
    title:str
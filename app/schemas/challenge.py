from datetime import datetime
from pydantic import BaseModel
from typing import List


class ChallengeBase(BaseModel): 
    title:str
    is_completed:bool
    date:datetime
    due_date:datetime

    
class ChallengeGet(ChallengeBase):
    id:int

class ChallengeListGet(BaseModel):
    challenges:List[ChallengeGet]


class ChallengeCreate(ChallengeBase):
    user_id:int 


class ChallengeEdit(ChallengeBase):
    ...
                                                                                                      


class ChallengeDelete(ChallengeBase):
    ...


class GetChallenge(ChallengeBase):
    ...



    


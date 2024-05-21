from datetime import datetime
<<<<<<< HEAD
from pydantic import BaseModel
from typing import List


class ChallengeBase(BaseModel): 
    date:datetime
    due_date:datetime
    title:str
    is_completed:bool

class ChallengeCreate(ChallengeBase):
    user_id:int 
   

class ChallengeGet(ChallengeBase):
    id:int
    user_id:int

class ChallengeEdit(ChallengeBase):
    ...


class ChallengeListGet(BaseModel):
    challenges:List[ChallengeGet]

                                                                               

class ChallengeDelete(ChallengeBase):
    ...


class GetChallenge(ChallengeBase):
    ...



    

=======
from typing import List

from pydantic import BaseModel


class ChallengeBase(BaseModel):
    date: datetime
    due_date: datetime
    title: str
    is_completed: bool


class ChallengeCreate(ChallengeBase):
    user_id: int


class ChallengeGet(ChallengeBase):
    id: int
    user_id: int


class ChallengeEdit(ChallengeBase): ...


class ChallengeListGet(BaseModel):
    challenges: List[ChallengeGet]


class ChallengeDelete(ChallengeBase): ...


class GetChallenge(ChallengeBase): ...
>>>>>>> 3954c7a96d9b40a741312ef6c04b3d20d47da27b

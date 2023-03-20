from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import random

origins = ["*"]

class student(BaseModel):
    name: str
    age: int
    srn: str
    comments: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post("/student")
async def create_student(student: student):
    student = jsonable_encoder(student)
    name= student['name']
    age= student['age']
    srn= student['srn']
    comments= student['comments']
    d= {'name':name,'age':age,'srn':srn,'comments':comments}
    f= open("student.txt","a")
    f.write(str(d))
    # f.write(f'{s_name},{str(age)},{srn}, {com} \n')
    f.close()
    with(open("funfacts.txt","r")) as f:
        data= f.readlines()
        a=(random.choice(data).strip())
    return 'hello '+name+' you are '+str(age)+f' old, and your data has been noted,\
     Did you know:- {a}'

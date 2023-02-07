import uvicorn
from fastapi import FastAPI, Request
from chatopenapi import get_info
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from db import db_insert
from models import Item


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    #return {"message": "Hello World"}
    return templates.TemplateResponse(name='index.html', context={'request': request, 'prompt': "怎么把别人的女朋友搞到手"})

@app.post("/chat")
def getinf(input: dict):
    problem = input['input']
    answer = get_info(problem)
    db_insert(problem, answer[1])
    return answer[1]


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5000, reload=True)
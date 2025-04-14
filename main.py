from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # return published
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'All unpublished blogs'}


@app.get('/blog/{id}')
def about(id: int):
    #Fetch blog with id, where id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # return limit
    return {'data': {'1', '2'}}


@app.post('/blog')
def create_blog(request: Blog):
    # return request
    return {'data': {f'Blog is created with the title: {request.title}'}}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
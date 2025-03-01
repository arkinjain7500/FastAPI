from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'data': {'name': 'Arkin Jain'}}

@app.get('/about')
def about():
    return {'data': 'About Page'}
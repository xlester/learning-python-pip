import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/')# ruta desde donde se podra ver la lista
def get_list():
    return [1,2,3,4,5,6]

@app.get('/contact')
def get_list():
    return {'name':'Orlando'}

@app.get('/web', response_class=HTMLResponse)
def get_html():
    return"""
    <h1>Mi pagina usando FastAPI</h1>
    <p>Para esto utilice HTMLResponse de FastAPI</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
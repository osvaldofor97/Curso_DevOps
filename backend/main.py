from fastapi import FastAPI

app = FastAPI()

# Se define ruta principal
@app.get("/")
def read_root():
    return {"Hello": "World"}

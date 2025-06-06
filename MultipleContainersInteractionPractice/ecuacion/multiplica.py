from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class Input(BaseModel):
    a: float
    b: float
    c: float
    d: float

@app.post("/resolver")
def resolver(valores: Input):
    suma_resp = requests.post("http://suma-service:8000/sumar", json={"a": valores.a, "b": valores.b})
    resta_resp = requests.post("http://resta-service:8000/restar", json={"c": valores.c, "d": valores.d})
    suma = suma_resp.json()["resultado"]
    resta = resta_resp.json()["resultado"]
    resultado = suma * resta
    return {"resultado": resultado}
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()


@app.exception_handler(500)
def internal_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content=jsonable_encoder({"code": 500, "msg": "Internal Server Error"}))


@app.post("/")
def func():
    raise ValueError

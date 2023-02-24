from fastapi import FastAPI

app = FastAPI()

items = {"a": "a1", "b": "b1", "c": "c1", "d": "d1"}


@app.get("/items/")
def root(query: str):
    if query in items:
        filtered = items[query]
    else:
        return "file doesnt exist"
    return filtered

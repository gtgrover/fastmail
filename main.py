from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, 
                 {"item_name": "Bar"}, 
                 {"item_name": "Baz"},
                 {"item_name": "Blaze"}]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(skip: int = 0, limit: int = 10):
    #, item_id: str = '', q: str = '' | None = None ):
    return fake_items_db[skip : skip + limit]
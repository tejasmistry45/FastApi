# https://fastapi.tiangolo.com/tutorial/query-params/

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "1_Foo"}, 
                 {"item_name": "2_Bar"}, 
                 {"item_name": "3_Raz"},
                 {"item_name": "4_Caz"},
                 {"item_name": "6_Daz"},
                 {"item_name": "7_Eaz"},
                 {"item_name": "8_Faz"}]

@app.get("/items/")
async def get_items(skip: int=0, limit: int = 10):
    return fake_items_db[skip: skip+limit]

# Example Try
# http://127.0.0.1:8000/items/
# http://127.0.0.1:8000/items/?skip=0&limit=10
# http://127.0.0.1:8000/items/?skip=20
# http://127.0.0.1:8000/items/?limit=3
'''
Create a simple FastAPI application that serves 3 endpoints:
    - GET /: Returns a greeting message.
    - GET /items/{item_id}: Returns a message with the item ID.
    - GET /items: Reruns a list of items.
'''

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items")
async def read_items():
    return {"items": ["item1", "item2", "item3"]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")

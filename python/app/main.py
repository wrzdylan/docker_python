import psycopg2
import os
from typing import Union

from fastapi import FastAPI
from dotenv import load_dotenv


app = FastAPI()


def db_conn():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB", "postgres"), 
        user="postgres", 
        password=os.getenv("POSTGRES_PASSWORD", "secret"),
        host="test",
    )

    print("Database connected successfully")

    return conn


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



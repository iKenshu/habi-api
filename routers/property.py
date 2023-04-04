from typing import Optional

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from config import database
from querys import sql_data
from querys.querys import query_all

property_router = APIRouter()


@property_router.get(path="/property/all/", tags=["home"], status_code=200)
def all_data():
    db = database.SessionLocal()
    data = sql_data.query(db, query_all)
    return JSONResponse(status_code=200, content=data)


@property_router.get(path="/property/", tags=["property"], status_code=200)
def get_data(
    status: Optional[str] = None,
    year: Optional[int] = None,
    city: Optional[str] = None,
):
    db = database.SessionLocal()
    query = sql_data.compare_params(status, year, city, query_all)
    data = sql_data.query(db, query)
    return JSONResponse(status_code=200, content=data)

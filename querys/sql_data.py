from typing import List

from sqlalchemy.sql import text


def query(db, sql_query) -> List[str]:
    """Function to execute raw SQL and format data to return it."""
    db_response = db.execute(text(sql_query))
    data = []
    for db in db_response:
        data_db = {
            "address": db[0],
            "city": db[1],
            "price": db[2],
            "description": db[3],
            "status": db[4],
        }
        data.append(data_db)
    return data


def two_params(status: str, year: int, city: str, query: str) -> str:
    """Function to compare more than one params and return the query"""
    if year and city:
        query += f"AND pt.year = {year} AND pt.city = '{city}'"
    elif year and status:
        query += f"AND pt.year = {year} AND st.name = '{status}'"
    elif status and city:
        query += f"AND st.name = '{status}' AND pt.city = '{city}'"
    return query


def compare_params(status: str, year: int, city: str, query: str) -> str:
    """Function to compare all the params and return the query"""
    if status and year and city:
        query += f"AND pt.year = {year} AND st.name = '{status}' AND pt.city = '{city}'"
    elif (status or year) and (city or status) and (city or year):
        query = two_params(status, year, city, query)
    elif year:
        query += f"AND pt.year = {year}"
    elif status:
        query += f"AND st.name = '{status}'"
    elif city:
        query += f"AND pt.city = '{city}'"
    return query

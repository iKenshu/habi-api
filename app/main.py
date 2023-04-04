from fastapi import FastAPI
from fastapi.responses import JSONResponse

from routers.property import property_router

app = FastAPI()
app.title = "Habi API"
app.include_router(property_router)


@app.get("/", tags=["Home"])
def home() -> None:
    message = {
        "Message": "Welcome, you have different options to use this API. /docs for documentation"
    }
    return JSONResponse(status_code=200, content=message)

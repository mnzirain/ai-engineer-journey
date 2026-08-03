from fastapi import FastAPI
import uvicorn

from config.settings import API_TITLE
from config.settings import API_VERSION

from api.routes import router

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION
)

app.include_router(router)


if __name__ == "__main__":

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
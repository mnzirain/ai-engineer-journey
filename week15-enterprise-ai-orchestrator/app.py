from fastapi import FastAPI

from api.routes import router
from config.settings import API_TITLE, API_VERSION

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION
)

app.include_router(router)


if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
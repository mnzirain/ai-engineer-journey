from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "Week 16 Enterprise Tool Calling Platform"
    version: str = "1.0.0"
    debug: bool = True


settings = Settings()
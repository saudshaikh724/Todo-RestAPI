from pydantic import BaseSettings


class CommonSettings(BaseSettings):
    APP_NAME: str = "Todo"
    DEBUG_MODE: bool = False


class ServerSettings(BaseSettings):
    HOST: str = "0.0.0.0"
    PORT: int = 8000


class DatabaseSettings(BaseSettings):
    DB_URL: str = "mongodb+srv://dbSaud:dbSaud3431@cluster0.zfckt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    DB_NAME: str = "tasks"


class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    pass


settings = Settings()

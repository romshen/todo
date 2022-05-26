from pydantic import BaseSettings


class Env(BaseSettings):
    DB_TYPE: str = "postgresql"
    USER_NAME: str = "postgres"
    PASSWORD: str = "%test-8329#"
    HOST: str = "127.0.0.1"
    PORT: str = "5432"
    DB_NAME: str = "test"

    class Config:
        env_file = ".env"


env = Env()

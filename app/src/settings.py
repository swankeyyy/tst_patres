class Settings:
    DB_URL = 'postgresql+asyncpg://library:library@localhost:5432/library'
    DB_ECHO = False
    TEST_DB_URL = 'postgresql+asyncpg://tst_db:tst_db@localhost:5433/tst_db'


settings = Settings()

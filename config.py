import os
import dotenv
dotenv.load_dotenv()
class Config:
    db_name = os.environ.get("DB_NAME")
    print(db_name)
    db_user = os.environ.get("DB_USER")
    db_pass = os.environ.get("DB_PASSWORD")
    db_port = os.environ.get("DB_PORT")
    db_host = os.environ.get("DB_HOST")

    def __init__(self):
        pass

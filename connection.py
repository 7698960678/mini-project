from config import Config
import psycopg2


class Connection:
    conn = None
    config = None

    def __init__(self):
        self.config = Config()

    def setupDbConnection(self):
        config = self.config
        if (config.db_host is None
                or config.db_user is None
                or config.db_pass is None
                or config.db_port is None
                or config.db_name is None):
            print("Please setup environment variables as mentioned in readme file.")
        else:
            self.conn = psycopg2.connect(database=config.db_name, user=config.db_user, password=config.db_pass,
                                         port=config.db_port, host=config.db_host)
            print(":::::::::::::::",self.conn)
        return self.conn

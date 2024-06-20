from .migration import Migration


class ChangeDB(Migration):
    def update(self):
        sql = """
            CREATE TABLE users (
                id bigserial,
                name varchar(100) not null,
                email varchar(100) not null,
                version varchar(100) not null,
                createdAt BIGINT NOT NULL,
                PRIMARY KEY (id)
            );
        """
        self.my_cursor.execute(sql)

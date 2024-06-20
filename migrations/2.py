from .migration import Migration


class ChangeDB(Migration):
    def update(self):
        sql = """
            CREATE TABLE hotel(
                id bigserial,
                name varchar(100),
                address varchar(100),
                number BIGINT NOT NULL,
                createdAt BIGINT NOT NULL,
                PRIMARY KEY (id)
            );
        """
        self.my_cursor.execute(sql)
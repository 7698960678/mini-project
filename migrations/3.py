from .migration import Migration


class ChangeDB(Migration):
    def update(self):
        sql = """
            CREATE TABLE room(
                id bigserial,
                name varchar(100) ,
                price float,
                hotelID int,
                createdAt BIGINT NOT NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (hotelID) REFERENCES hotel(id)
            );
        """
        self.my_cursor.execute(sql)

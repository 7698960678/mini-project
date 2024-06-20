from .migration import Migration


class ChangeDB(Migration):
    def update(self):
        sql = """
            CREATE TABLE payment(
                id bigserial,
                price float ,
                bookingID int,
                createdAt BIGINT,
                PRIMARY KEY (id),
                FOREIGN KEY (bookingID) REFERENCES booking(id)
            );
        """
        self.my_cursor.execute(sql)

from .migration import Migration


class ChangeDB(Migration):
    def update(self):
        sql = """
            CREATE TABLE booking(
                id bigserial,
                name varchar(100),
                price int,
                bookingdate TIMESTAMP ,
                hotelID int,
                roomID int,
                createdAt BIGINT,
                PRIMARY KEY (id),
                FOREIGN KEY (hotelID) REFERENCES hotel(id),
                FOREIGN KEY (roomID) REFERENCES room(id)
            );
        """
        self.my_cursor.execute(sql)

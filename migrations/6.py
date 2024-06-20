from .migration import Migration


class ChangeDB(Migration):
    def update(self):
        sql = """
            ALTER TABLE booking
            DROP COLUMN hotelID;

            ALTER TABLE room
            ADD type varchar(255);

            ALTER TABLE room
            RENAME COLUMN type to room_type;

            ALTER TABLE room
            ALTER COLUMN price TYPE TIMESTAMP USING to_timestamp(price);

            ALTER TABLE booking
            ALTER COLUMN price TYPE VARCHAR(100);
        """
        self.my_cursor.execute(sql)
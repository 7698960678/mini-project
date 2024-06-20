

class Utils:
    @staticmethod
    def is_table_exists(my_cursor, table_name):
        my_cursor.execute("SELECT EXISTS (SELECT FROM pg_tables WHERE schemaname ='public' and tablename = %s)",
                          (table_name,))
        return my_cursor.fetchone()[0]


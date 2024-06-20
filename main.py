import importlib
import os
import re
from connection import Connection
from utils import Utils


class Main:
    conn = None
    my_cursor = None
    migration_steps_dir = 'migrations'
    migration_file_pattern = re.compile(r"^([0-9]*)\.py$")
    is_upgrade_table_exist = False
    current_migration = 0

    def __init__(self):
        self.conn = Connection().setupDbConnection()

    ###############################################
    # Get a current migration number from upgrade table.
    ###############################################
    def get_current_migration(self):
        try:
            self.my_cursor.execute('SELECT version FROM users ORDER BY id DESC LIMIT 1')
            result = self.my_cursor.fetchall()
            current_db_version = result[0][0] if result else 0
            return int(current_db_version)
        except Exception as e:
            print(str(e))
            return str(e)

    ############################################################
    # Execute a update method written inside each migration file
    ############################################################
    def execute_one_by_one(self, version):
        try:
            print("executing migration {}.py".format(version))

            mod = importlib.import_module("migrations.{}".format(version))
            klass = getattr(mod, 'ChangeDB')
            klass(self.my_cursor, self.conn).update()
        except Exception as e:
            print(str(e))
            return str(e)

    ########################################################
    # Execute migrations one by one.
    ########################################################
    def execute_migrations(self, migrations):
        try:
            for migration in migrations:
                self.execute_one_by_one(migration)

            if len(migrations) >= 1:
                self.my_cursor.execute(
                    "INSERT INTO users (version, name, email, createdAt) VALUES (%s,'testing', 'super@gmail.com', EXTRACT(EPOCH FROM CURRENT_TIMESTAMP));",
                    (migrations[-1],))
                self.conn.commit()
                self.my_cursor.execute(
                    "INSERT INTO hotel (name, address, number, createdAt) VALUES ('vivanta','ahmedabad', 8965326, EXTRACT(EPOCH FROM CURRENT_TIMESTAMP));",
                    (migrations[-1],))
                self.conn.commit()
                self.my_cursor.execute(
                    "INSERT INTO booking (name, price, bookingdate, createdAt) VALUES ('markzug',8965326, CURRENT_TIMESTAMP, EXTRACT(EPOCH FROM CURRENT_TIMESTAMP));",
                    (migrations[-1],))
                self.conn.commit()
                print("successfully upgraded")
            else:
                print("nothing to upgrade")
        except Exception as e:
            print(e)
            self.conn.rollback()
        finally:
            self.my_cursor.close()
            self.conn.close()

    ###################################################
    # Get all migration files as per pattern.
    ###################################################
    def migration_files(self):
        all_migration_file_names = (next(os.walk(self.migration_steps_dir))[2])
        return list(map(lambda file_name: int(self.migration_file_pattern.match(file_name).group(1))
        if bool(self.migration_file_pattern.match(file_name)) else -1, all_migration_file_names))

    ###########################################################
    # Get a list of migration numbers/files that to be executed
    ###########################################################
    def get_new_migrations(self):
        return sorted(list(filter(lambda migration: migration > self.current_migration, self.migration_files())))

    def migrate(self):
        if self.conn is None:
            print("111111")
            print("Migration is not started, Please resolve mentioned errors.")
            return
        try:
            print("22222")
            self.my_cursor = self.conn.cursor()
            self.is_upgrade_table_exist = Utils.is_table_exists(self.my_cursor, "users")

            if self.is_upgrade_table_exist:
                # get a current migration number from upgrade table.
                self.current_migration = self.get_current_migration()

            # run all the migrations which are newer then the current migration in the db
            migrations = self.get_new_migrations()

            # execute the migrations
            print("migrations to be executed: {}".format(migrations))
            self.execute_migrations(migrations)
        except Exception as e:
            print(":::::",e)


def startDBMigration():
    Main().migrate()

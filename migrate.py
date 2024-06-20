import sys
from main import Main

def print_help():
    print("""
It creates a new table into database `upgrade` if doesn't exist & sets a value of 
version to 1. If `upgrade` is already present then finds a last executed version and starts executing script after 
that number. Scripts should be present inside `migrations` folder. After successful execution a new row will be 
created inside `upgrade` table. A version will be a number of last execute py file inside a `migrations` folder.
Please note you should be giving a py file name in form of incremental numbers.""")


input_param = None if len(sys.argv) == 1 else sys.argv[1]
if input_param in ["-h", "--help"]:
    print_help()
else:
    print("starting a database migration")
    Main().migrate()

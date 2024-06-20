# okuloop-db-migration

Repo for Database Migration of Okuloop

- Create virtual Environment

  1. Install : pip install virtualenv
  2. Created virtual env : virtualenv myenv
  3. activate : . myenv/local/bin/activate

- pip install -r requirements.txt

- Set an environment variable by creating a new file named ".env."

  - Set up your database credentials
    DB_USER="postgres"
    DB_PASSWORD="123"
    DB_PORT="5432"
    DB_NAME="postgres"
    DB_HOST="127.0.0.1"

- Run all migration scripts `python migrate.py` or `python3 migrate.py`

not working env in window 
1. Change Execution Policy (Temporary):
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
2. Activate the Virtual Environment:
.\myenv\Scripts\Activate
3. Revert Execution Policy:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Default

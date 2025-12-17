# Connecting to ODS via Python

## Step 1 — Install python packages

Run in GitBash:
> ```bash
> conda activate
> pip install sqlalchemy oracledb
> ```

####

## Step 2 — Set up Connection in Python

Open up an existing/launch new Jupyter Notebook, or open a Python Script via VSC.
> To launch a new jupyter notebook:
> - Open up Anaconda
> - Click `Launch Jupyter`
> - Navigate to the appropriate directory
> - Click `New`

Set up Connection by copy-pasting and running the following python code
<mark>Note: update user and password as needed.</mark>
> ```python
> from sqlalchemy import create_engine
> 
> USER = "ud_tableau_read"
> PWD  = <password from Keeper>
> HOST = "ban-odsp-db1.servers.udayton.edu"
> PORT = 1521
> SERVICE = "odsp.servers.udayton.edu"
> 
> engine = create_engine(
>    f"oracle+oracledb://{USER}:{PWD}@{HOST}:{PORT}/?service_name={SERVICE}"
> )
> ```

####

## Step 3 — Write & Execute a SQL Command in Python

SQL in Python Example:
> ```python
> sql = """
> SELECT <...>
> FROM <schema>.<table>
> <...>
> """
> ```

Execute SQL command with the engine via pandas
> ```python
> df = pd.read_sql(sql, engine)
> ```

####

Examples

1. Load UD_STUDENT_COURSE
> ```python
> sql = """
> SELECT *
> FROM UD_STUDENT.UD_STUDENT_COURSE
> """
>
> df_enrl = pd.read_sql(sql, engine)
> ```

####

2. List all Schemas
> ```python
> sql = """
> SELECT DISTINCT owner
> FROM all_tab_columns
> ORDER BY owner
> """
> df_schemas = pd.read_sql(sql, engine)
> df_schemas
> ```

####

3. List all tables in the UD_STUDENT schema
> ```python
> sql = """
> SELECT DISTINCT table_name
> FROM all_tab_columns
> WHERE owner = 'UD_STUDENT'
> ORDER BY table_name
> """
> df_tables = pd.read_sql(sql, engine)
> df_tables
> ```

####
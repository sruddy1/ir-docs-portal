# Connecting to ODS via Python

## Step 1: Install python packages
>
> - Open up GitBash
>```bash
> conda activate
> pip install sqlalchemy oracledb
> ```
####
## Step 2: Set up Connection in Python
>
> - Open up an existing Jupyter Notebook, Python Script via VSC, or Launch a New Jupyter Notebook.
>> To launch a new jupyter notebook:
>> - Open up Anaconda
>> - Click `Launch Jupyter`
>> - Navigate to the appropriate directory
>> - Click `New`
>
> - Set up Connection by copy-pasting the following python code
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
## Step 3: Write a SQL Command
>
> - SQL in Python looks like
> ```python
> sql = """
> SELECT <...>
> FROM <schema>.<table>
> <...>
> """
> ```
>
> - Execute SQL command with the engine via pandas
> ```python
> df = pd.read_sql(sql, engine)
> ```
>####
> Examples
>
> - Load UD_STUDENT_COURSE
> ```python
> sql = """
> SELECT *
> FROM UD_STUDENT.UD_STUDENT_COURSE
> """
>
> df_enrl = pd.read_sql(sql, engine)
> ```
>####
>
> - List all Schemas
> ```python
> sql = """
> SELECT DISTINCT owner
> FROM all_tab_columns
> ORDER BY owner
> """
> df_schemas = pd.read_sql(sql, engine)
> df_schemas
> ```
>####
>
> - List all tables in the UD_STUDENT schema
> ```python
> sql = """
> SELECT DISTINCT table_name
> FROM all_tab_columns
> WHERE owner = 'UD_STUDENT'
> ORDER BY table_name
> """
> df_tables = pd.read_sql(sql, engine)
> df_tables



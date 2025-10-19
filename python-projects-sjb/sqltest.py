import subprocess
import json
import pyodbc
import struct

server = 'dvdtitles.database.windows.net'
database = 'dvdtitles'
driver = '{ODBC Driver 17 for SQL Server}'

# Get token by running az CLI command manually
result = subprocess.run(
    ['az', 'account', 'get-access-token', '--resource', 'https://database.windows.net/', '--output', 'json'],
    capture_output=True,
    text=True,
    check=True
)

token_json = json.loads(result.stdout)
token = token_json['accessToken']

exptoken = bytes(token, "UTF-8")
tokenstruct = struct.pack(f"<I{len(exptoken)}s", len(exptoken), exptoken)

conn_str = f"DRIVER={driver};SERVER={server};DATABASE={database};Authentication=ActiveDirectoryAccessToken"

with pyodbc.connect(conn_str, attrs_before={1256: tokenstruct}) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
        for row in cursor.fetchall():
            print(row.name, row.collation_name)

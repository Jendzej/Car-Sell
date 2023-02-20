import os

import oracledb
from dotenv import load_dotenv

load_dotenv()

cs = '''(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)
    (port=1521)(host=adb.eu-frankfurt-1.oraclecloud.com))
    (connect_data=(service_name=g874014763bc302_projects_high.adb.oraclecloud.com))
    (security=(ssl_server_dn_match=yes)))'''

connection = oracledb.connect(
    user="admin",
    password=os.getenv("ORACLE_PASSWORD"),
    dsn=cs
)
cursor = connection.cursor()

cursor.execute("DROP TABLE test")
cursor.execute("""CREATE TABLE test(test_id number(10) primary key, test_name varchar2(10))""")
connection.close()

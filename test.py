import psycopg2
import os
from project.mysql_api import Mydb_scrap


# Update connection string information
host = "youcefscrap.postgres.database.azure.com"
dbname = "postgres"
user = "youcef@youcefscrap"
password = "Satellite93@"
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()
d1 = "100321"
d2 = "200321"
cursor.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Date(Date_num)>=Date(%s) AND Date(Date_num)<=Date(%s);", (d1, d2))
result = cursor.fetchall()
print(result)
# Clean up
conn.commit()
cursor.close()
conn.close()
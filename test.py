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
equipe = "Real madrid"
cursor.execute("SELECT Nom, Date_text, Time, Chaine FROM Match WHERE Equipe1 LIKE %s OR Equipe2 LIKE %s;", (equipe, equipe))
#cursor.execute("SELECT * FROM Match limit 10;")
result = cursor.fetchall()
print(result)
# Clean up
conn.commit()
cursor.close()
conn.close()
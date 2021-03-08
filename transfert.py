import psycopg2
import os
from project.mysql_api import Mydb_scrap
from dotenv import load_dotenv

load_dotenv()
# Update connection string information
host = os.getenv('ENV_HOST')
dbname = os.getenv('ENV_dbname')
user = os.getenv('ENV_user')
password = os.getenv('ENV_MDP')
sslmode = "require"

conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")

cursor = conn.cursor()

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS Match_t;")
print("Finished dropping table (if existed)")

cursor.execute("CREATE TABLE Match_t (id serial PRIMARY KEY, Nom VARCHAR(100) NOT NULL, Date_text VARCHAR(100), Time VARCHAR(20), Equipe1 VARCHAR(100), Equipe2 VARCHAR(100), Competition VARCHAR(100), Chaine VARCHAR(100), Date_num VARCHAR(100));")
print("Finished creating table")

test = Mydb_scrap()
data = test.recup()

# for i in data[5:]:
#     list_i = list(i)
#     ii = list_i[1:]
#     tuple_i = tuple(ii)
#     sql  = "INSERT INTO Matchs (Nom, Date_text, Time, Equipe1, Equipe2, Competition, Chaine, Date_num) VALUES {value};".format(value=tuple_i)
#     cursor.execute(sql)
for ii, i in enumerate(data):
    list_i = list(data[ii])
    list_ii = list_i[1:]
    if list_ii[1] == "Aujourd'hui":
        list_ii[1] = "xxx"
    tuple_i = tuple(list_ii)
    sql  = "INSERT INTO Match (Nom, Date_text, Time, Equipe1, Equipe2, Competition, Chaine, Date_num) VALUES {value};".format(value=tuple_i)
    cursor.execute(sql)

cursor.execute("SELECT * FROM Match limit 10;")
result = cursor.fetchall()
print(result)
# Clean up
conn.commit()
cursor.close()
conn.close()
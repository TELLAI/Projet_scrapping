import psycopg2
import os
from dotenv import load_dotenv

class Mydb_scrap:
    def __init__(self):
        self.host = os.getenv('ENV_HOST')
        self.dbname = os.getenv('ENV_dbname')
        self.user = os.getenv('ENV_user')
        self.password = os.getenv('ENV_MDP')
        self.sslmode = "require"
        self.mydb = psycopg2.connect("host={0} user={1} dbname={2} password={3} sslmode={4}".format(self.host, self.user, self.dbname, self.password, self.sslmode))
        self.mycursor=self.mydb.cursor()

    def create_table(self):
        self.mycursor.execute("DROP TABLE IF EXISTS Match_t;")
        self.mycursor.execute("CREATE TABLE Match_t (id serial PRIMARY KEY, Nom VARCHAR(100) NOT NULL, Date_text VARCHAR(100), Time VARCHAR(20), Equipe1 VARCHAR(100), Equipe2 VARCHAR(100), Competition VARCHAR(100), Chaine VARCHAR(100), Date_num VARCHAR(100));")

    def insert_table(self, data):
        for i in data:
            val = tuple(i.values())
            #print(val)
            db_keys = ", ".join(i.keys())
            #print(db_keys)
            sql  = "INSERT INTO Match_t ({columns}) VALUES {value};".format(columns=db_keys, value=val)
            self.mycursor.execute(sql)
            self.mydb.commit()

    def recup(self):
        sql = "SELECT * FROM Match_t;"
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        return result

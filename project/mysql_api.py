import mysql.connector

class Mydb_scrap:
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="pw",
                    database= "scrap",
                    auth_plugin='mysql_native_password'
                )
        self.mycursor=self.mydb.cursor()

    def create_table(self):
        self.mycursor.execute("""CREATE TABLE IF NOT EXISTS Matchs_t (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Nom VARCHAR(100) NOT NULL, Date_text VARCHAR(100), Time VARCHAR(20), Equipe1 VARCHAR(100), Equipe2 VARCHAR(100), Competition VARCHAR(100), Chaine VARCHAR(100), Date_num VARCHAR(100));""")

    def insert_table(self, data):
        for i in data:
            val = tuple(i.values())
            #print(val)
            db_keys = ", ".join(i.keys())
            #print(db_keys)
            sql  = "INSERT INTO Matchs_t ({columns}) VALUES {value};".format(columns=db_keys, value=val)
            self.mycursor.execute("use scrap;")
            self.mycursor.execute(sql)
            self.mydb.commit()

    def recup(self):
        sql = "SELECT * FROM Matchs_t;"
        self.mycursor.execute("use scrap;")
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        return result

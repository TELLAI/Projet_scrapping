import mysql.connector
import datetime

class Week_foot:
    def __init__(self):
        self.mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="pw",
                    database= "scrap",
                    auth_plugin='mysql_native_password'
                )
        self.mycursor=self.mydb.cursor()
        self.data= ""
        self.date1 = ""
        self.date2 = ""

    def date(self):
        dates = datetime.date.today()
        j = str(dates.day)
        if len(list(j)) == 1:
            j = "0" + j
        m = list(str(dates.month))
        if len(m) == 1:
            m.insert(0, "0")
            m = "".join(m)
        else:
            m = "".join(m)
        yyyy = list(str(dates.year))
        yy = "".join(yyyy[2:])
        self.date1 = j+m+yy
        j = str(int(j) + 1)
        if len(list(j)) == 1:
            j = "0" + j
        self.date2 = j+m+yy

    def equipe(self):
        equipe = "Real madrid"
        self.mycursor.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Equipe1 LIKE %s OR Equipe2 LIKE %s;", (equipe, equipe))
        self.data = self.mycursor.fetchall()
    def search(self):
        self.mycursor.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Date(Date_num)>=Date(%s) AND Date(Date_num)<=Date(%s);", (self.date1, self.date2))
        self.data = self.mycursor.fetchall()
test = Week_foot()
test.date()
test.search()
print(test.date1)
print(test.date2)
print(test.data)
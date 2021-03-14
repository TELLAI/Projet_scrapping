from api_scrap import Scrap_info
from mysql_api import Mydb_scrap

db = Mydb_scrap()
db.create_table()
data = Scrap_info()
data.finder()
db.insert_table(data.matchs)
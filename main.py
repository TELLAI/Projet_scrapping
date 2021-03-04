import logging
from project.api_scrap import Scrap_info
from project.mysql_api import Mydb_scrap
from project.route_flask import *

logging.basicConfig(level=logging.DEBUG,
                    filename="LOG_scrap.log",
                    filemode="a", #append ou W pour écraser
                    format='%(asctime)s : %(levelname)s : %(message)s')

def main():
    logging.info("\n\n-------------------init __main__.py------------------------ \n")
    try:
        db = Mydb_scrap()
        logging.info("Creation of instance of class Mydb_scrap")
    except:
        logging.info("Creation of instance of class Mydb_scrap not possible")
    try:
        db.create_table()
        logging.info("Creation of table in db")
    except:
        logging.info("Creation of table in db not possible")
    try:
        data = Scrap_info()
        data.finder()
        db.insert_table(data.matchs)
        logging.info("Insert information in table of db")
    except:
        logging.info("Insert information in table of db not possible")


if __name__=='__main__':
    app.run(host="0.0.0.0", port=5200, debug=True)
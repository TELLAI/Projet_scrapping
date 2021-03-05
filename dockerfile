FROM python:latest
COPY . .
RUN pip install mysql-connector flask_mysql_connector flask_cors flask psycopg2
CMD python main.py
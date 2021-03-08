FROM python:latest
COPY . .
RUN pip install mysql-connector flask_mysql_connector flask_cors flask bs4 datetime prettify requests
CMD python project/route_flask.py
EXPOSE 5000
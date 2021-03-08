FROM python:latest
COPY . .
RUN pip flask psycopg2 python-dotenv
CMD python project/route_flask.py
EXPOSE 4000
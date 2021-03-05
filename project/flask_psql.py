import psycopg2
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "host=youcefscrap.postgres.database.azure.com port=5432 dbname=postrges user=youcef@youcefscrap password=Satellite93@ sslmode=require"'

mysql = SQLAlchemy(app)

@app.route('/home', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        equipe = request.form['eq1']
        d1 = request.form['d1']
        d2 = request.form['d2']
        if equipe == "" and d1 != "" and d2 != "":
            return redirect(url_for('Date', d1=d1, d2=d2))
        elif equipe != "" and d1 == "" and d2 == "":
            return redirect(url_for('Team', equipe=equipe))
        else:
            return redirect(url_for('index'))
    else:
        return render_template('home.html')

@app.route('/Date/<d1>/<d2>', methods=['GET', 'POST'])
def Date(d1, d2):
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Date(Date_num)>=Date(%s) AND Date(Date_num)<=Date(%s);", (d1, d2))
    result = cur.fetchall()
    if len(result) == 0:
        data = []
        val = "Votre recherches ne correspond à aucun resultat"
        data.append(val)
        result.append(data)        
    return render_template("equipe.html", result=result)

@app.route('/Equipe/<equipe>', methods=['GET', 'POST'])
def Team(equipe):
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute("SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Equipe1 LIKE %s OR Equipe2 LIKE %s;", (equipe, equipe))
    result = cur.fetchall()
    if len(result) == 0:
        data = []
        val = "Votre recherches ne correspond à aucun resultat"
        data.append(val)
        result.append(data)
    return render_template("equipe.html", result=result)

@app.route('/Affiche')
def Affiche():
    list_equipe = ["Real Madrid", "Barcelone", "Liverpool", "Atlético", "Chelsea", "Manchester C.", "Manchester U.", "Milan", "Leceister", "Marseille OM", "Lyon OL", "Naples", "Tottenham", "Inter", "Arsenal", "Paris PSG", "Dortmund", "Bayern", "Benfica", "Juventus"]
    req = "SELECT Nom, Date_text, Time, Chaine FROM Matchs_t WHERE Equipe1 in ("
    for ii, i in enumerate(list_equipe):
        if ii == len(list_equipe) - 1:
            req = req + "'" + i + "') AND Equipe2 in ("
        else:
            req = req + "'" + i + "', "
    for jj, j in enumerate(list_equipe):
        if jj == len(list_equipe) - 1:
            req = req + "'" + j + "');"
        else:
            req = req + "'" + j + "', "
    
    cur = mysql.connection.cursor()
    cur.execute("use scrap;")
    cur.execute(req)
    result = cur.fetchall()
    cur.close()
    return render_template("equipe.html", result=result)


if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
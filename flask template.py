from flask import Flask
from flask import request, render_template
app = Flask(__name__)
import psycopg2

def add(name,surname):
    conn = psycopg2.connect(dbname='webbase', user='postgres', password='yuliy2908', host='127.0.0.1')
    curs = conn.cursor()
    curs.execute('''INSERT INTO webtable(nam, surname)
	VALUES ('{0}', '{1}')'''.format(name,surname))
    conn.commit()
    conn.close()

def upd(name,surname,tname,tsurname):
    conn = psycopg2.connect(dbname='webbase', user='postgres', password='yuliy2908', host='127.0.0.1')
    curs = conn.cursor()
    curs.execute('''SELECT id FROM webtable WHERE nam = '{0}' AND surname = '{1}' '''.format(name,surname))
    id = curs.fetchone()[0]
    if tname != '':
         curs.execute('''UPDATE webtable SET nam = '{0}' WHERE id = {1}'''.format(tname,id))
    if tsurname != '':
        curs.execute('''UPDATE webtable SET surname = '{0}' WHERE id = {1}'''.format(tsurname,id))
    conn.commit()
    conn.close()


@app.route('/', methods=['post', 'get'])
def index():
    message = ''
    name = ''
    surname = ''
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
    if name != '' and surname != '':
        add(name, surname)
    else:
        message = " Not all"
    tname = ''
    tsurname = ''
    id_name = ''
    id_surname = ''
    if request.method == 'POST':
        id_name = request.form.get('id_name')
        id_surname = request.form.get('id_surname')
        tname = request.form.get('cg_name')
        tsurname = request.form.get('cg_surname')
    if name != '' and surname != '':
        upd(id_name, id_surname, tname, tsurname)


    conn = psycopg2.connect(dbname='webbase', user='postgres', password='yuliy2908', host='127.0.0.1')
    curs = conn.cursor()
    curs.execute('''SELECT surname, nam from webtable ''')
    data = curs.fetchall()
    return render_template('index.html', data=data, message=message)


if __name__ == '__main__':
    app.run(debug=True)
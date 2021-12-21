from flask import Flask
from flask import request, make_response, redirect, abort
app = Flask(__name__)

users = [{'username': 'jpetrov', 'name': 'John', 'surname': 'Petrov', 'age': '19'},
 {'username': 'vivanov', 'name': 'Vasya', 'surname': 'Ivanov', 'age': '22'}]

@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/users')

@app.route('/ya')
def yandex():
    return redirect('http://yandex.ru')

@app.route('/users')
def print_user():
    data = ''
    for i in users:
        data += "<a href = '/users/{0}'> {0} </a> <br>".format(i['username'])
    return data

@app.route('/users/<username>')
def prof(username):
    usernames = []
    for index in users:
        usernames.append(index['username'])
    if username in usernames:
        i = usernames.index(username)
        return users[i]['name'] +" " + users[i]['surname'] + " " +users[i]['age']
    else:
        return "404: Not found"



@app.route('/user/<name>')
def user(name):
    return '<h1>username, %s</h2>' % name

@app.route('/user/<int:user_id>')
def user_id(user_id):
    return '<h2>user_id, %i</h2>' % user_id

if __name__ == '__main__':
    app.run(debug=True)


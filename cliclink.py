from flask import Flask
from flask import redirect, abort
app = Flask(__name__)


users = [{'username': 'jpetrov', 'name': 'John', 'surname': 'Petrov', 'age': '19'},
 {'username': 'vivanov', 'name': 'Vasya', 'surname': 'Ivanov', 'age': '22'}]

@app.route('/')
def index():
    return redirect('http://127.0.0.1:5000/users')

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
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)


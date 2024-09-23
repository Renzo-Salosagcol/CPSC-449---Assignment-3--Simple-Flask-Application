from flask import Flask,redirect, url_for, render_template

app = Flask(__name__)

users = {"users": [

{"id": 1, "username": "john_doe", "email": "john@example.com"},

{"id": 2, "username": "renzo_salosagcol", "email": "renzosalosagcol@csu.fullerton.edu"},

{"id": 3, "username": "alice_jones", "email": "alice@example.com"}

]}

@app.route('/')
def index():
  return render_template("index.html", users=users)

@app.route('/user/<id>')
def user_id(id):
  return render_template("display.html", users=users, user_id=int(id))
      
if __name__ == "__main__":
  app.run(debug=True)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ah:ah@localhost:5432/ah' #<dialect>://user:pass@<host>:<port>/<dbname>
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Person(db.Model):
    # __tablename__ = 'people' <-- if you want to change tablename
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.debug=True
    app.run(port=3000)
   
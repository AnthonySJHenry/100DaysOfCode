from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ah:ah@localhost:5432/ah' #<dialect>://user:pass@<host>:<port>/<dbname>
db = SQLAlchemy(app)



@app.route('/')
def index():
    return '<h1>Hello</h1>'

if __name__ == '__main__':
    app.debug=True
    app.run(port=3000)
   
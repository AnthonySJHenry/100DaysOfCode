from importlib.util import LazyLoader
from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ah:ah@localhost:5432/todoapp' #<dialect>://user:pass@<host>:<port>/<dbname>
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    list = db.relationship('Todo', backref="list")
    def __repr__(self):
        return f"{self.id}: {self.name}" 

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    desc = db.Column(db.String(), nullable=True)
    complete = db.Column(db.Boolean, nullable=True)
    list_id = db.Column(db.Integer, db.ForeignKey("list.id")) 
    
    def __repr__(self):
        return f"{self.name}: {self.desc}"



#db.create_all()
#HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
@app.route('/delete/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:     
        db.session.delete(Todo.query.get(todo_id))
        db.session.commit()
    except:
        db.session.rollback()
        print("error:",sys.exc_info())
    finally:
        db.session.close()
        
    return render_template('index.html', tasks=Todo.query.order_by('id').all())

@app.route('/completed/<todo_id>', methods=['POST'])
def completed_todo(todo_id):
    try:
        data = request.get_json()
        isComplete = data['isComplete']
        Todo.query.get(todo_id).complete = isComplete
        Todo.query.order_by(Todo.id).all()
        db.session.commit()
    except:
        db.session.rollback()
        print("error:",sys.exc_info())
    finally:
        db.session.close()
        
    
    return redirect("/")

@app.route('/create', methods=['POST'])
def create_todo():
    #body={}
    error = False
    try: 
        data = request.get_json()
        name = data['name']
        desc = data['desc']
        todo = Todo(name=name, desc=desc)
        # body['name'] = todo.name
        # body['desc'] = todo.desc
        db.session.add(todo)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
        print("\n\nERROR INFO:", sys.exc_info(), end="\n\n")
    finally:
        db.session.close()
        if  error == True:
            abort(400)
        else:            
            return redirect("/")

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', tasks=Todo.query.order_by('id').all())
 
#USING .env this time    
# if __name__ == '__main__':
#     app.env = 'development'
#     app.run()
#andremo a creare delle classi speciali che chiameremo modelli queste classi rappresenteranno
#le tabelle che verrano poi aggiunte al nostro database.7
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from blog import db, login_manager

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  #abbiamo il nome del campo, db.Column è una colonna del dabase, la tipologia ed eventuali altri parametri
  created_at = db.Column(db.DateTime, default=datetime.now)
  #ci servirà per sapere quando un istanza viene creata
  username = db.Column(db.String(12), unique=True, nullable=False)
  # specifica che lo username non può superare i 12 caratteri e che deve essere unico e non può essere vuoto
  email = db.Column(db.String(50), unique=True, nullable=False)
  password = db.Column(db.String(250), nullable=False)
  posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
  #questo è un campo relazionale che ci permette di accedere ad i post senza fare particolari interrogazioni al database 
  #queste vengono fatte per noi in maniera automatica con il backref e lazy ciu permette di fare operazioni di filtraggio 
  def __repr__(self):
    return f"User('{ self.id }', '{ self.username }', '{ self.email }')"

  def set_password_hash(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)


class Post(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  #ad ogni post verrà associata la chiave primaria di chi ha scritto il post
  created_at = db.Column(db.DateTime, default=datetime.now)
  title = db.Column(db.String(120), nullable=False)
  description = db.Column(db.String(240))
  body = db.Column(db.Text(), nullable=False)
  slug = db.Column(db.String(250))
  image = db.Column(db.String(120))

  def __repr__(self):
    return f"Post('{ self.id }', '{ self.title }')"

import os

basedir = os.path.abspath(os.path.dirname(__file__))
#all'interno della nostra variabile è presente la locazione del nostro file

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'blog.db')
  #abbiamo configurato dove è allocato il nostro dabase e specificato un nome 'blog.db'
  SLQALCHEMY_TRACK_MODIFICATIONS = False 
  #serve per prenire l'invio di segnali in fase di modifica che non abbiamo bisogno
  UPLOAD_FOLDER = "static/img/posts"
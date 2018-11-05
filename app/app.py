from flask import Flask
from models import db

app = Flask(__name__)

POSTGRES = {
    'name': 'phone',
    'id': '1',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route("/")
def main():
    return 'Hello World !'

if __name__ == '__main__':
    app.run()
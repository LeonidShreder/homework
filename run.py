from app import app, db
from app.models import categories, post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
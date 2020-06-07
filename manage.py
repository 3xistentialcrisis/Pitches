from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.models import User

app = create_app()

manager = Manager(app)
migrate = Migrate(app,db
manager.add_command('run',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

# Create Flask-script shell
@manager.shell
def make_shell_context():
    return dict(app = app,db = db, User = User )


if __name__ == "__main__":
    manager.run

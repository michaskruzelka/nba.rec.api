from flask_script import Manager
from flask_migrate import MigrateCommand
from api import create_app

app = create_app()

manager = Manager(app)
manager.add_command("db", MigrateCommand)


@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000)


@manager.command
def runworker():
    app.run(debug=False)


if __name__ == "__main__":
    manager.run()

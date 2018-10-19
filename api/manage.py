from flask.cli import FlaskGroup

from project import api

cli = FlaskGroup(api)

if __name__ == '__main__':
    cli()
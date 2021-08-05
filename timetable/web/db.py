import timetable_lib
from timetable_lib import init_db
import click
from flask import g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = timetable_lib.get_db()

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

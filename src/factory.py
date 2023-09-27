import sys

from flask import Flask

from .celery import init_celery, celery
from .config import Config, logger
from src.modules.index.controller import index_bp


def create_application():

    logger.info('Starting app')

    app = Flask(__name__, template_folder='templates')
    app.config.from_object(Config)

    sys.stdout.flush()

    app.register_blueprint(index_bp)

    init_celery(app, celery)

    app.app_context().push()

    return app

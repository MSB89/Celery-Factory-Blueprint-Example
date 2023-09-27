import logging
import os
from enum import Enum
from typing import Optional
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Config(object):
    DOMAIN = os.environ.get('DOMAIN')
    SERVER_NAME = os.environ.get('DOMAIN')

    SECRET_KEY: Optional[str] = os.environ.get('SECRET_KEY')

    CELERY_RESULT_BACKEND: Optional[str] = os.getenv('CELERY_RESULT_BACKEND')
    CELERY_BROKER_URL: Optional[str] = os.getenv('CELERY_BROKER_URL')


logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()

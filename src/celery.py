from celery import Celery


def init_celery(app, celery):
    celery.conf.update(app.config)
    task_base = celery.Task

    class ContextTask(task_base):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)

    celery.Task = ContextTask


celery = Celery('src.application', backend='rpc://')
from src.tasks import example_task

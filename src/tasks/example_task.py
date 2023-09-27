from src.celery import celery

from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@celery.task
def example_task():
    logger.info(f"Task Executed")

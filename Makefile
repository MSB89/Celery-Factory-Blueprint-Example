requirements:
	pip install -r requirements.txt
run:
	gunicorn --reload src.wsgi --log-level DEBUG
run-worker:
	celery -A src.celery worker --loglevel=info

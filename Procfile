web: gunicorn run:app
worker: celery -A swizzl.routes:celery worker --loglevel=info

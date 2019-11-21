from celery import Celery

app = Celery('tasks',broker='redis://localhost:6379')

@app.task
def reverse(string):
	return string[::-1]
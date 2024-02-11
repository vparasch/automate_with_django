from automateWithDjango.celery import app
import time


@app.task
def celery_test_task():
    time.sleep(10)  # simulate a task that takes 10 seconds
    return 'Task executed successfully'

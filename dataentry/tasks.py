import logging

from django.core.management import call_command

from automateWithDjango.celery import app
import time


@app.task
def celery_test_task():
    time.sleep(10)  # simulate a task that takes 10 seconds
    return 'Task executed successfully'


@app.task()
def import_data_task(full_path, model_name):
    # trigger the import data command to insert the csv contents in the database
    try:
        call_command('importdata', full_path, model_name)
    except Exception as e:
        logging.exception('error importing data')
        raise e
    return 'Data inserted successfully'

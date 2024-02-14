import csv
import logging

from django.apps import apps
from django.core.management.base import CommandError
from django.db import DataError


def search_for_model(model_name):
    # search for the model across all installed apps
    model = None

    for app_config in apps.get_app_configs():
        # try to search for the model
        try:
            model = apps.get_model(app_config.label, model_name)
            break  # stop searching if model found
        except LookupError:
            continue  # basically keep searching in other apps
    if not model:
        raise CommandError(f'Model "{model_name}" not found')

    return model


# Get all custom models in all installed apps
def get_all_custom_models():
    default_models = ['Permission', 'Group', 'ContentType', 'Session', 'LogEntry', 'User', 'Upload']
    all_models = []
    for app_config in apps.get_app_configs():
        for model in app_config.get_models():
            if model.__name__ not in default_models:
                all_models.append(model.__name__)
    return all_models


def check_csv_errors(file_path, model_name):
    # Search all the apps for the model name given
    model = search_for_model(model_name)

    # Compare csv header with the model fields names
    model_fields = [field.name for field in model._meta.fields if field.name != 'id']  # exclude id field

    try:
        with open(file_path, 'r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames

            # Compare csv header with the model fields names
            if csv_header != model_fields:
                raise DataError(f'CSV file header does not match the {model_name} table field names')
    except Exception as e:
        raise e

    return model, reader
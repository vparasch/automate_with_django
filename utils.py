from django.apps import apps
from django.core.management.base import CommandError


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

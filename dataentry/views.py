from django.shortcuts import render, redirect
from django.conf import settings
from utils import get_all_custom_models
from uploads.models import Upload
from django.contrib import messages
from .tasks import import_data_task


# We want to store the uploaded file but also store its contents in the database
def import_data(request):
    if request.method == 'POST':
        # The file path need .FILES because check line 23 input typ = file
        # The model name need.POST because check line 28 it is a simple select
        file_path = request.FILES.get('file_path')  # this file_path is in the importdata.html file line 23
        model_name = request.POST.get('model_name')  # this model_name is in the importdata.html file line 29

        # store the file in the Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        # construct the full path
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)

        full_path = base_url + relative_path

        # check for csv errors

        # handle the task
        import_data_task.delay(full_path, model_name)

        messages.info(request, 'Your data is being imported, '
                               'you will be notified when is it finished')
        # redirect to the import data page
        return redirect('import_data')
    else:
        # We need all the models in order to get the context so we can iterate through them in the html file
        all_custom_models = get_all_custom_models()
        context = {'all_custom_models': all_custom_models}
    return render(request, 'dataentry/importdata.html', context=context)

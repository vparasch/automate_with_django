from django.contrib import admin
from .models import Upload


# Register your models here.

# In the admin panel i want to display the following arguments
class UploadAdmin(admin.ModelAdmin):
    list_display = ('file', 'model_name', 'uploaded_at')


admin.site.register(Upload, UploadAdmin)

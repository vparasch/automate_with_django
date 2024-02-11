from django.contrib import admin
from .models import Student, Customer, Employee


# Register your models here.

# In the admin panel i want to display the following arguments
# TODO: TRY ADDING SORTING BY ROLL NO, NAME AND AGE


class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_no', 'name', 'age')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'country')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'employee_name', 'designation')


admin.site.register(Student, StudentAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Employee, EmployeeAdmin)

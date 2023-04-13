from django.utils.html import format_html
from django.contrib import admin
from .models import Department, Employee

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department',)
    search_fields=('department',)
    ordering=('department',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone_number','dateJoined','department','display_image')
    search_fields=('first_name','last_name','email','phone_number','department',)
    ordering=('department',)

    def display_image(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.profile_picture.url))
        else:
            return None

    display_image.short_description = 'Image'
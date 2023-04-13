from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

from .models import Department, Employee

# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=('department','view_employees_link',)
    search_fields=('department',)
    ordering=('department',)

    def view_employees_link(self, obj):
        count = obj.employee_set.count()
        url = (
            reverse("admin:employment_employee_changelist")
            + "?"
            + urlencode({"department__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">( {} ) Employees</a>', url, count)

    view_employees_link.short_description = "Employees"

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone_number','dateJoined','department','display_image')
    search_fields=('first_name','last_name','phone_number','department',)
    list_filter=('department','dateJoined',)
    ordering=('department',)
    readonly_fields = ('image_tag',)

    def display_image(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="80" height="70" />'.format(obj.profile_picture.url))
        else:
            return None

    display_image.short_description = 'Image'

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        if obj:
            fieldsets += (
                ('profile picture', {
                    'fields': (('profile_picture', 'image_tag'),)
                }),
            )
        return fieldsets

    def image_tag(self, obj):
        return format_html('<img src="{}" height="250em"/>'.format(obj.profile_picture.url))
    display_image.short_description = 'Profile'

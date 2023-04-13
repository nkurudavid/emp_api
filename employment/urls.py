from django.conf.urls import url
from employment import views

urlpatterns = [
    url(r'^department$', views.departmentApi, name='department'),
    url(r'^department/([0-9]+)$',)
]
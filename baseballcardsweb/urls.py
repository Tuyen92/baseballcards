from rest_framework import routers
from django.urls import include, path
from . import views

r = routers.DefaultRouter()
r.register('/employees', views.EmployeesViewGet)
r.register('/new_employee', views.EmployeesViewCreate)
r.register('/skills', views.SoftskillsViewGet)
r.register('/new_language', views.LanguagesViewCreate)
r.register('/new_soft_skill', views.SoftskillsViewCreate)
r.register('/new_hard_skill', views.HardskillsViewCreate)

urlpatterns = [
    path('api', include(r.urls)),
    path('', views.index),
    path('new_employee', views.new_employee),
    path('skills_form', views.skills_form),
]
from rest_framework import routers
from django.urls import include, path
from . import views

r = routers.DefaultRouter()
r.register('employees', views.EmployeesViewGet)
r.register('new_employee', views.EmployeesViewCreate)
r.register('skills', views.SoftskillsViewGet)
r.register('new_language', views.LanguagesViewCreate)
r.register('new_soft_skill', views.SoftskillsViewCreate)
r.register('new_hard_skill', views.HardskillsViewCreate)
r.register('new_emp_language', views.EmployeeLanguageViewCreate)
r.register('new_emp_softskill', views.EmployeeSoftskillViewCreate)
r.register('new_emp_hardskill', views.EmployeeHardskillViewCreate)
r.register('new_reference', views.ReferenceViewCreate )
r.register('reference/', views.ReferenceViewGet)

urlpatterns = [
    path('api/', include(r.urls)),
    path('', views.index),
    path('new_employee', views.new_employee),
    path('odoo_site', views.odoo_connection),
    path('skills_form', views.skills_form),
]
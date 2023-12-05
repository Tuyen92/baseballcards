from typing import Any
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.views import View
from rest_framework.views import Response
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from rest_framework.test import APIRequestFactory
from .admin import EmployeesForm
from .models import *
from .serializers import *
from .form import *
from .odoo_connection import OdooConnection
from rest_framework.permissions import IsAuthenticated
import requests

# Create your views here.

def odoo_connection(request):
    factory = APIRequestFactory()
    # fields_info = OdooConnection.model.execute_kw(OdooConnection.db, OdooConnection.uid, OdooConnection.password, 'hr.employee', 'fields_get', [], {'attributes': ['string', 'type']})
    odoo_data = OdooConnection.model.execute_kw(OdooConnection.db, OdooConnection.uid, OdooConnection.password, "hr.employee", "search_read", [[]], {'fields': ['name', 'gender', 'address', 'birthday', 'work_phone', 'work_email', 'notes', 'image_medium', 'em_level', 'speciality']})
    # print(odoo_data)
    employee_data = {}
    for od in odoo_data:
        # if Levels.objects.filter(level=(od['em_level'])).exists() and Specialities.objects.filter(speciality=(od['speciality'])).exists():
        # level = Levels.objects.filter(level=(od['em_level']))
        # speciality = Specialities.objects.get(speciality=(od['speciality']))
        if od['em_level'] != False and od['speciality'] != False:
            employee_data = {
                    # 'odoo_id': od['id'],
                    'full_name': od['name'],
                    'gender': od['gender'],
                    'address': od['address'],
                    'image': "AA",
                    'phone': od['work_phone'],
                    'birthday': '2023-04-12',
                    'email': od['work_email'],
                    'bio': od['notes'],
                    "level": od['em_level'][0],
                    "speciality": od['speciality'][0]
                }
            request_api = factory.post("/api/new_employee/", employee_data)
            response = EmployeesViewCreate.as_view({'post': 'create'})(request_api)
            print(response)
    data = {
        'odoo_data': odoo_data
    }
    return render(request, 'odoo_site.html', context=data)


def index(request):
    data, languages, soft_skills, hard_skills = [], [], [], []
    employees_view = EmployeesViewGet.as_view({'get': 'list'})
    employees = employees_view(request).data
    for employee in employees:
        languages = EmployeeLanguages.objects.filter(employee=employee['id'])
        hard_skills = EmployeeHardskills.objects.filter(employee=employee['id'])
        soft_skills = EmployeeSoftskills.objects.filter(employee=employee['id'])
        data.append({
            'employee': employee,
            'languages': languages,
            "soft_skills": soft_skills,
            'hard_skills': hard_skills,
        })
    employee_data = {
        'employees': data
    }
    return render(request, 'index.html', context=employee_data)


def new_employee(request):    
    context = {}
    factory = APIRequestFactory()

    # LOAD DATA INTO FORM
    employees = Employees.objects.all()
    soft_skills = Softskills.objects.all()
    hard_skills = Hardskills.objects.all()
    languages = Languages.objects.all()
    levels = Levels.objects.all()
    specialities = Specialities.objects.all()

    # INPUT FORM FOR EMPLOYEE
    form = NewEmployeeForm
    level_form = LevelsForm
    ref_form = NewReferencesForm

    # ADD NEW SKILL
    language = LanguageForm
    soft_skill = SoftskillsForm
    hard_skill = HardskillsForm
    emp_language_form = NewEmployeeLanguagesForm
    emp_soft_skill_form = NewEmployeeSoftskillForm
    emp_hard_skill_form = NewEmployeeHardskillForm
    
    if request.method.__eq__("POST") and 'create_employee' in request.POST:
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            employee_data = { 
                'full_name': form.cleaned_data['full_name'],
                'gender': form.cleaned_data['gender'],
                'address': form.cleaned_data['address'],
                'image': form.cleaned_data['image'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'bio': form.cleaned_data['bio'],
                "level": Levels.objects.get(level=form.cleaned_data['level']).id,
                "speciality":  Specialities.objects.get(speciality=form.cleaned_data['speciality']).id
            }
            request_api = factory.post("/api/new_employee/", employee_data)
            response = EmployeesViewCreate.as_view({'post': 'create'})(request_api)

            odoo_employee = OdooConnection.model.execute_kw(OdooConnection.db, OdooConnection.uid, OdooConnection.password, "hr.employee", "create", [
                {
                    'name': employee_data['full_name'],
                    'gender': employee_data['gender'],
                    'address': employee_data['address'],
                    # 'image': ImageSend,
                    # 'birthday': '2023-11-11',
                    'phone': employee_data['phone'],
                    'work_email': employee_data['email'],
                    'notes': employee_data['bio'],
                    'em_level': 1,
                    'speciality': 'software engineer'
                }])
            form.clean()
        else:
            print("CAN NOT ADD NEW EMPLOYEE")
            form.clean()

    elif request.method.__eq__("POST") and 'add_language' in request.POST:
        language_form = LanguageForm(request.POST)
        emp_language_form = NewEmployeeLanguagesForm(request.POST)
        employee = NewReferencesForm(request.POST)
        if language_form.is_valid():
            language_data = language_form.cleaned_data['language']
            if Languages.objects.filter(language=language_data).exists() == False:
                request_data = {
                    'language': language_data
                }
                request_api = factory.post("/api/new_language/", request_data)

                response = LanguagesViewCreate.as_view({'post': 'create'})(request_api)
                language_form.clean()

            elif emp_language_form.is_valid():
                employee = emp_language_form.cleaned_data['employee']
                language_id = Languages.objects.get(language=language_data).id
                if EmployeeLanguages.objects.filter(language=language_id, employee=employee.id).exists() == False:
                    request_data = {
                        'employee': employee.id,
                        'language': language_id,
                        'rate': emp_language_form.cleaned_data['rate']
                    }
                    print(request_data)
                    request_api = factory.post("/api/new_emp_language/", request_data)

                    response = EmployeeLanguageViewCreate.as_view({'post': 'create'})(request_api)
                    emp_language_form.clean()
            else:
                print("INVALID FORM OF LANGUAGE")
                language_form.clean()
                emp_language_form.clean()

    elif request.method.__eq__("POST") and 'add_soft_skill' in request.POST:
        soft_skill_form = SoftskillsForm(request.POST)
        emp_soft_skill_form = NewEmployeeSoftskillForm(request.POST)
        if soft_skill_form.is_valid():
            soft_skill_data = soft_skill_form.cleaned_data['soft_skill']
            if Softskills.objects.filter(soft_skill=soft_skill_data).exists() == False:
                request_data = {
                    'soft_skill': soft_skill_data
                }
                request_api = factory.post("/api/new_soft_skill/", request_data)
                response = SoftskillsViewCreate.as_view({'post': 'create'})(request_api)
                soft_skill_form.clean()

            elif emp_soft_skill_form.is_valid():
                employee = emp_soft_skill_form.cleaned_data['employee']
                soft_skill_id = Softskills.objects.get(soft_skill=soft_skill_data).id
                if EmployeeSoftskills.objects.filter(soft_skill=soft_skill_id, employee=employee.id).exists() == False:
                    request_data = {
                        'employee': employee.id,
                        'soft_skill': soft_skill_id,
                        'rate': emp_soft_skill_form.cleaned_data['rate']
                    }
                    print(request_data)
                    request_api = factory.post("/api/new_emp_softskill/", request_data)

                    response = EmployeeSoftskillViewCreate.as_view({'post': 'create'})(request_api)
                    emp_soft_skill_form.clean()
            else:
                print("INVALID FORM OF SOFT SKILL")
                soft_skill_form.clean()
                emp_soft_skill_form.clean()
        

    elif request.method.__eq__("POST") and 'add_hard_skill' in request.POST:
        hard_skill_form = HardskillsForm(request.POST)
        emp_hard_skill_form = NewEmployeeHardskillForm(request.POST)
        if hard_skill_form.is_valid():
            hard_skill_data = hard_skill_form.cleaned_data['hard_skill']
            if Hardskills.objects.filter(hard_skill=hard_skill_data).exists() == False:
                request_data = {
                    'hard_skill': hard_skill_data
                }
                request_api = factory.post("/api/new_hard_skill/", request_data)

                response = HardskillsViewCreate.as_view({'post': 'create'})(request_api)
                hard_skill_form.clean()

            elif emp_hard_skill_form.is_valid():
                employee = emp_hard_skill_form.cleaned_data['employee']
                hard_skill_id = Hardskills.objects.get(hard_skill=hard_skill_data).id
                if EmployeeHardskills.objects.filter(hard_skill=hard_skill_id, employee=employee.id).exists() == False:
                    request_data = {
                        'employee': employee.id,
                        'hard_skill': hard_skill_id,
                        'rate': emp_hard_skill_form.cleaned_data['rate']
                    }
                    request_api = factory.post("/api/new_emp_hardskill/", request_data)

                    response = EmployeeHardskillViewCreate.as_view({'post': 'create'})(request_api)
                    emp_hard_skill_form.clean()
            else:
                print("INVALID FORM OF HARD SKILL")
                hard_skill_form.clean()
                emp_hard_skill_form.clean()

    elif request.method.__eq__("POST") and 'adding_reference' in request.POST:
        ref_form = NewReferencesForm(request.POST)
        if ref_form.is_valid():
            employee = ref_form.cleaned_data['employee']
            if Reference.objects.filter(employee=employee.id).exists == False:
                request_data = {
                    'employee': employee.id,
                    'cv': ref_form.cleaned_data['cv'],
                    'linkedin': ref_form.cleaned_data['linkedin']
                }
                request_api = factory.post("/api/new_reference/", request_data)

                response = ReferenceViewCreate.as_view({'post': 'create'})(request_api)
                ref_form.clean()
            else:
               pass
        else:
            print('INVALID FORM OF REFERENCES')
            ref_form.clean()
            
    context['form'] = form
    return render(request, 'employee_form.html', {
        'form': form, 
        'emp_soft_skill_form': emp_soft_skill_form,
        'emp_hard_skill_form': emp_hard_skill_form,
        'employee_language': emp_language_form,
        'ref_form': ref_form, 
        'employees': employees, 
        'soft_skills': soft_skills,
        'hard_skills': hard_skills,
        'soft_skill': soft_skill,
        'hard_skill': hard_skill,
        'levels': levels,
        'level_form': level_form,
        'specialities': specialities,
        'languages': languages,
        'language': language 
    })


def skills_form(request):
    context = {}
    employees = Employees.objects.all()
    languages = NewEmployeeLanguagesForm()
    return render(request, 'employee_skills.html', {'employees': employees, 'languages': languages})


class EmployeesViewGet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class SoftskillsViewGet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Softskills.objects.all()
    serializer_class = SoftskillsSerializer


class LanguagesViewGet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer


class EmployeeLanguagesViewGet(viewsets.ViewSet, generics.ListAPIView):
    queryset = EmployeeLanguages.objects.all()
    serializer_class = EmployeeLanguagesSerializer


class ReferenceViewGet(viewsets.ViewSet, generics.ListAPIView, generics.RetrieveAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer


# CREATE
class EmployeesViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeeCreateSerializer
        

class LanguagesViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesCreateSerializer


class SoftskillsViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Softskills.objects.all()
    serializer_class = SoftskillsCreateSerializer


class HardskillsViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Hardskills.objects.all()
    serializer_class = HardskillsCreateSerializer


class EmployeeLanguageViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Languages.objects.all()
    serializer_class = EmployeeLanguagesCreateSerializer


class EmployeeSoftskillViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = EmployeeLanguages.objects.all()
    serializer_class = EmployeeSoftSkillCreateSerializer


class EmployeeHardskillViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = EmployeeHardskills.objects.all()
    serializer_class = EmployeeHardSkillCreateSerializer


class ReferenceViewCreate(viewsets.ViewSet, generics.CreateAPIView):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer

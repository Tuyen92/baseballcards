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
from rest_framework.permissions import IsAuthenticated
import requests

# Create your views here.

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
    form = NewEmployeeForm()
    level_form = LevelsForm()
    employee_languages = EmployeeLanguagesForm()
    ref_form = NewReferencesForm()

    # ADD NEW SKILL
    language = LanguageForm()
    soft_skill = SoftskillsForm()
    hard_skill = HardskillsForm()
    emp_soft_skill_form = EmployeeSoftskillForm()
    emp_hard_skill_form = EmployeeHardskillForm()
    
    if request.method.__eq__("POST") and 'create_employee' in request.POST:
        print("HERE")
        form = NewEmployeeForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['level'])
            employee_data = { 
                'full_name': form.cleaned_data['full_name'],
                'sex': form.cleaned_data['sex'],
                'address': form.cleaned_data['address'],
                'image': form.cleaned_data['image'],
                'phone': form.cleaned_data['phone'],
                'email': form.cleaned_data['email'],
                'bio': form.cleaned_data['bio'],
                "level": Levels.objects.get(level=form.cleaned_data['level']).id,
                "speciality":  Specialities.objects.get(speciality=form.cleaned_data['speciality']).id
            }
            print(employee_data)
            request_api = factory.post("/api/new_employee/", employee_data)
            new_employee = EmployeesViewCreate.as_view({'post': 'create'})
            response = new_employee(request_api)
            print(response.data)
            form.clean()
        else:
            print("CAN NOT ADD NEW EMPLOYEE")
            form.clean()

            # return redirect('/')

    elif request.method.__eq__("POST") and 'add_language' in request.POST:
        language_form = LanguageForm(request.POST)
        if language_form.is_valid():
            language_data = language_form.cleaned_data['language']
            if Languages.objects.filter(language=language_data).exists() == False:
                request_data = {
                    'language': language_data
                }
                request_api = factory.post("/api/new_language/", request_data)

                new_language = LanguagesViewCreate.as_view({'post': 'create'})
                response = new_language(request_api)
                language_form.clean()
            else:
                print("CAN NOT ADD NEW LANGUAGE")
                language_form.clean()

    elif request.method.__eq__("POST") and 'add_soft_skill' in request.POST:
        soft_skill_form = SoftskillsForm(request.POST)
        if soft_skill_form.is_valid():
            soft_skill_data = soft_skill_form.cleaned_data['soft_skill']
            if Softskills.objects.filter(soft_skill=soft_skill_data).exists() == False:
                request_data = {
                    'soft_skill': soft_skill_data
                }
                request_api = factory.post("/api/new_soft_skill/", request_data)

                new_soft_skill = SoftskillsViewCreate.as_view({'post': 'create'})
                response = new_soft_skill(request_api)
                soft_skill_form.clean()
            else:
                print("CAN NOT ADD NEW SOFT SKILL")
                soft_skill_form.clean()

    elif request.method.__eq__("POST") and 'add_hard_skill' in request.POST:
        hard_skill_form = HardskillsForm(request.POST)
        if hard_skill_form.is_valid():
            hard_skill_data = hard_skill_form.cleaned_data['hard_skill']
            if Hardskills.objects.filter(hard_skill=hard_skill_data).exists() == False:
                request_data = {
                    'hard_skill': hard_skill_data
                }
                request_api = factory.post("/api/new_hard_skill/", request_data)

                new_hard_skill = HardskillsViewCreate.as_view({'post': 'create'})
                response = new_hard_skill(request_api)
                hard_skill_form.clean()
            else:
                print("CAN NOT ADD NEW HARD SKILL")
                hard_skill_form.clean()

    elif request.method.__eq__("POST") and 'adding_reference' in request.POST:
        ref_form = NewReferencesForm(request.POST)
        if ref_form.is_valid():
            ref_form.save()
            return redirect('/')
        else:
            print('CAN NOT ADD REFERENCES')

    
            
    context['form'] = form
    return render(request, 'employee_form.html', {
        'form': form, 
        'emp_soft_skill_form': emp_soft_skill_form,
        'emp_hard_skill_form': emp_hard_skill_form,
        'ref_form': ref_form, 
        'employees': employees, 
        'soft_skills': soft_skills,
        'hard_skills': hard_skills,
        'soft_skill': soft_skill,
        'hard_skill': hard_skill,
        'levels': levels,
        'level_form': level_form,
        'specialities': specialities,
        'employee_language': employee_languages,
        'languages': languages,
        'language': language 
    })


def add_ref(request):
    context = {}
    employees = EmployeesForm()
    ref_form = NewReferencesForm()
    if request.method == "POST" and 'create_skill' in request.POST:
        ref_form = NewReferencesForm(request.POST)
        if ref_form.is_valid():
            ref_form.save()
        else:
            print('CAN NOT ADD REFERENCES')
        # context['skill_form'] = skill_form
    return render(request, 'info_form.html', {'employees': employees, 'ref_form': ref_form})


def skills_form(request):
    context = {}
    employees = Employees.objects.all()
    languages = EmployeeLanguagesForm()
    return render(request, 'employee_skills.html', {'employees': employees, 'languages': languages})

# def new_language(request):
#     employees = Employees.objects.all()
#     if request.method.__eq__("POST") and 'add_language' in request.POST:
#         language_form = LanguageForm(request.POST)
#         print('here')
#         if language_form.is_valid():
#             print("OK")
#             language_data = language_form.cleaned_data
#             add_languages(language_data)
#     return render(request, 'employee_skills.html', {'employees': employees})


# def add_languages(language):
#     print(language)
#     data = {
#         "language": language
#     }
#     api_endpoint = "http://127.0.0.1:8000/api/new_language"
#     response = requests.post(api_endpoint, data=data)
#     print(response)
#     if response.status_code == 201:
#         print("Language cretae successfully")
#     else:
#         print(f"Failed to create language. Status code: {response.status_code}, Repsonse: {response.text}")
#     return response.text

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
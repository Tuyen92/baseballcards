from rest_framework.serializers import ModelSerializer
from .models import *


class SoftskillsSerializer(ModelSerializer):
    class Meta:
        model = Softskills
        fields = ['id', 'soft_skill']


class EmployeeSoftskillsSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSoftskills
        fields = ['id', 'soft_skill', 'employee', 'rate']


class HardskillsSerializer(ModelSerializer):
    class Meta:
        model = Softskills
        fields = ['id', 'hard_skill']


class EmployeeHardskillsSerializer(ModelSerializer):
    class Meta:
        model = EmployeeHardskills
        fields = ['id', 'hard_skill', 'employee', 'rate']


class LanguagesSerializer(ModelSerializer):
    class Meta:
        model = Languages
        fields = ['id', 'language']


class EmployeeLanguagesSerializer(ModelSerializer):
    class Meta:
        model = EmployeeLanguages
        fields = ['id', 'language', 'rate']


class LevelSerializer(ModelSerializer):
    class Meta:
        model = Levels
        fields = ['id', 'level', 'color']


class SpecialitySerializer(ModelSerializer):
    class Meta:
        model = Specialities
        fields = ['id', 'speciality', 'color']


class EmployeeSerializer(ModelSerializer):
    # soft_skills = EmployeeSoftskillsSerializer(many=True)
    # hard_skills = EmployeeHardskillsSerializer(many=True)
    # languages = EmployeeLanguagesSerializer(many=True)
    level = LevelSerializer()
    speciality = SpecialitySerializer()
    class Meta:
        model = Employees
        fields = ['id', 'full_name', 'gender', 'address', 'phone', 'image', 'bio', 'level', 'speciality']


# CREATE
class LevelCreateSerializer(ModelSerializer):
    class Meta:
        model = Levels
        fields = ['id', 'level']


class SpecialityCreateSerializer(ModelSerializer):
    class Meta:
        model = Specialities
        fields = ['id', 'speciality']


class EmployeeCreateSerializer(ModelSerializer):
    class Meta:
        model = Employees
        fields = ['full_name', 'gender', 'address', 'image', 'phone', 'email', 'bio', 'level', 'speciality']


class LanguagesCreateSerializer(ModelSerializer):
    class Meta:
        model = Languages
        fields = ['language']


class SoftskillsCreateSerializer(ModelSerializer):
    class Meta:
        model = Softskills
        fields = ['soft_skill']


class HardskillsCreateSerializer(ModelSerializer):
    class Meta:
        model = Hardskills
        fields = ['hard_skill']


class EmployeeLanguagesCreateSerializer(ModelSerializer):
    class Meta:
        model = EmployeeLanguages
        fields = ['employee', 'language', 'rate']


class EmployeeSoftSkillCreateSerializer(ModelSerializer):
    class Meta:
        model = EmployeeSoftskills
        fields = ['employee', 'soft_skill', 'rate']


class EmployeeHardSkillCreateSerializer(ModelSerializer):
    class Meta:
        model = EmployeeHardskills
        fields = ['employee', 'hard_skill', 'rate']


class ReferenceSerializer(ModelSerializer):
    class Meta:
        model = Reference
        fields = ['employee', 'cv', 'linkedin']
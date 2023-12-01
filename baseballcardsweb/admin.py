from django.contrib import admin
from .models import *
from django import forms

# Register your models here.
class EmployeesForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'


class EmployeesAdmin(admin.ModelAdmin):
    form = EmployeesForm


class SoftskillsForm(forms.ModelForm):
    class Meta:
        model = Softskills
        fields = '__all__'


class SoftskillsAdmin(admin.ModelAdmin):
    form = SoftskillsForm


class EmployeeSoftskillsForm(forms.ModelForm):
    class Meta:
        model = EmployeeSoftskills
        fields = '__all__'


class EmployeeSoftskillsAdmin(admin.ModelAdmin):
    form = EmployeeSoftskillsForm


class HardskillsForm(forms.ModelForm):
    class Meta:
        model = Hardskills
        fields = '__all__'


class HardskillsAdmin(admin.ModelAdmin):
    form = HardskillsForm


class EmployeeHardskillsForm(forms.ModelForm):
    class Meta:
        model = EmployeeHardskills
        fields = '__all__'


class EmployeeHardskillsAdmin(admin.ModelAdmin):
    form = EmployeeHardskillsForm


class LanguagesForm(forms.ModelForm):
    class Meta:
        model = Languages
        fields = '__all__'


class LanguagesAdmin(admin.ModelAdmin):
    form = LanguagesForm


class EmployeeLanguagesForm(forms.ModelForm):
    class Meta:
        model = EmployeeLanguages
        fields = '__all__'


class EmployeeLanguagesAdmin(admin.ModelAdmin):
    form = EmployeeLanguagesForm


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = '__all__'


class ReferenceAdmin(admin.ModelAdmin):
    form = ReferenceForm


class LevelsForm(forms.ModelForm):
    class Meta:
        model = Levels
        fields = '__all__'


class LevelsAdmin(admin.ModelAdmin):
    form = LevelsForm


class SpecialitiesForm(forms.ModelForm):
    class Meta:
        model = Specialities
        fields = '__all__'


class SpecialitiesAdmin(admin.ModelAdmin):
    form = SpecialitiesForm


admin.site.register(Employees, EmployeesAdmin)
admin.site.register(Softskills, SoftskillsAdmin)
admin.site.register(Hardskills, HardskillsAdmin)
admin.site.register(Languages, LanguagesAdmin)
admin.site.register(Levels, LevelsAdmin)
admin.site.register(Specialities, SpecialitiesAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(EmployeeSoftskills, EmployeeSoftskillsAdmin)
admin.site.register(EmployeeHardskills, EmployeeHardskillsAdmin)
admin.site.register(EmployeeLanguages, EmployeeLanguagesAdmin)

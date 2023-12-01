from django import forms
from .models import *


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['full_name', 'bio', 'phone', 'sex', 'address', 'level', 'speciality']


class LevelsForm(forms.ModelForm):
    class Meta:
        model = Levels
        fields = ['id', 'level']


class SpecialitiesForm(forms.ModelForm):
    class Meta:
        model = Specialities
        fields = ['id', 'speciality']


class NewEmployeeForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Full name",
        "class": "form-control"
    }), required=False)

    options = (('1', 'Male'), ('0', 'Female'))
    sex = forms.IntegerField(widget=forms.Select(choices=options , attrs={
        "class": "form-control"
    }), required=False)

    bio = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Bio...",
        "class": "form-control limited-line-textarea",
        "maxlength": 200
    }), required=False)

    address = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Address",
        "class": "form-control"
    }), required=False)

    phone = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Phone",
        "class": "form-control"
    }), required=False)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder": "Email",
        "class": "form-control"
    }), required=False)

    birth = forms.DateField(widget=forms.DateInput(format=('%d/%m/%Y'), attrs={
        "placeholder": "Select a date",
        "class": "form-control",
        "type": "date"
    }), required=False)

    image = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Image link",
        "class": "form-control"
    }), required=False)

    level = forms.ModelChoiceField(queryset=Levels.objects.all(), widget=forms.Select(choices=Levels.objects.all(), attrs={
        "class": "form-control"
    }), required=False)

    speciality = forms.ModelChoiceField(queryset=Specialities.objects.all(), widget=forms.Select(choices=Specialities.objects.all(), attrs={
        "class": "form-control"
    }), required=False)

    class Meta:
        model = Employees
        fields = ['full_name', 'bio', 'phone', 'sex', 'address', 'image', 'email', 'speciality']


class EmployeeSoftskillForm(forms.ModelForm):
    soft_skill = forms.ModelChoiceField(queryset=Softskills.objects.all() ,widget=forms.Select(choices=Softskills.objects.all(), attrs={
        "placeholder": "Skill title",
        "class": "form-control"
    }), required=False)

    level = (('1', '1 star'), ('2', '2 stars'), ('3', '3 stars'), ('4', '4 stars'), ('5', '5 stars'))
    rate = forms.IntegerField(widget=forms.Select(choices=level, attrs={
        "class": " form-control"
    }), required=False)

    class Meta:
        model = EmployeeSoftskills
        fields = ['soft_skill', 'rate']


class EmployeeHardskillForm(forms.ModelForm):
    hard_skill = forms.ModelChoiceField(queryset=Hardskills.objects.all(), widget=forms.TextInput(attrs={
        "placeholder": "Skill title",
        "class": "form-control"
    }), required=False)

    level = (('1', '1 star'), ('2', '2 stars'), ('3', '3 stars'), ('4', '4 stars'), ('5', '5 stars'))
    rate = forms.IntegerField(widget=forms.Select(choices=level, attrs={
        "class": " form-control"
    }), required=False)

    class Meta:
        model = EmployeeHardskills
        fields = ['hard_skill', 'rate']


class NewReferencesForm(forms.ModelForm):
    employee = forms.ModelChoiceField(queryset=Employees.objects.all(), widget=forms.Select(choices=Employees.objects.all(), attrs={
        "class": "form-control"
    }), required=False)

    cv = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your CV",
        "class": "form-control"
    }), required=False)

    linkedin = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Your Linkedin",
        "class": "form-control"
    }), required=False)

    class Meta:
        model = Reference
        fields = ['employee', 'cv', 'linkedin']


class EmployeeLanguagesForm(forms.ModelForm):
    language = forms.ModelChoiceField(queryset=Languages.objects.all(), widget=forms.Select(choices=Languages.objects.all(), attrs={
        "class": "form-control"
    }), required=False)

    level = (('1', '1 star'), ('2', '2 stars'), ('3', '3 stars'), ('4', '4 stars'), ('5', '5 stars'))
    rate = forms.IntegerField(widget=forms.Select(choices=level, attrs={
        "class": " form-control"
    }), required=False)

    class Meta:
        model = EmployeeLanguages
        fields = ['id', 'language', 'rate']


class LanguageForm(forms.ModelForm):
    language = forms.CharField(widget=forms.TextInput(attrs={
        "id": "language",
        "class": "form-control",
        "placeholder": "Language",
        "autocomplete": "off",
        "onclick": "showOptions('language_options')",
        "onkeyup": "filterLanguages()",
    }), required=False)

    class Meta:
        model = Languages
        fields = ['language']


class SoftskillsForm(forms.ModelForm):
    soft_skill = forms.CharField(widget=forms.TextInput(attrs={
        "id": "soft_skill",
        "class": "form-control",
        "placeholder": "Skill title",
        "autocomplete": "off",
        "onclick": "showOptions('soft_options')",
        "onkeyup": "filterSearch('soft_skill', 'soft_options')",
    }), required=False)

    class Meta:
        model = Softskills
        fields = ['soft_skill']


class HardskillsForm(forms.ModelForm):
    hard_skill = forms.CharField(widget=forms.TextInput(attrs={
        "id": "hard_skill",
        "class": "form-control",
        "placeholder": " Skill title",
        "autocomplete": "off",
        "onclick": "showOptions('hard_options')",
        "onkeyup": "filterSearch('hard_skill', 'hard_options')",
    }), required=False)

    class Meta:
        model = Hardskills
        fields = ['hard_skill']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Username",
        "class": "form-control"
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Password",
        "class": "form-control"
    }))


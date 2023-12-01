# Generated by Django 4.2.7 on 2023-11-29 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('sex', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255, null=True)),
                ('birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('bio', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hardskills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hard_skill', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Softskills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soft_skill', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Specialities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.employees')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeSoftskills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.employees')),
                ('soft_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.softskills')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.levels'),
        ),
        migrations.AddField(
            model_name='employees',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.specialities'),
        ),
        migrations.CreateModel(
            name='EmployeeLanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.employees')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.languages')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeHardskills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=1)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.employees')),
                ('hard_skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baseballcardsweb.hardskills')),
            ],
        ),
    ]

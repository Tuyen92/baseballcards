# Generated by Django 4.2.7 on 2023-12-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseballcardsweb', '0005_remove_employees_sex_employees_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
# Generated by Django 4.2.7 on 2023-12-06 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baseballcardsweb', '0009_rename_odoo_id_employees_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='image1',
            field=models.ImageField(null=True, upload_to='baseballcardweb/static/images'),
        ),
    ]

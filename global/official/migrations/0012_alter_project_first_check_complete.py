# Generated by Django 5.0.1 on 2024-01-05 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0011_alter_project_first_check_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='first_check_complete',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]

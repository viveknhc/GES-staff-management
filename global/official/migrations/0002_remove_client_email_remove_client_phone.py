# Generated by Django 4.2.3 on 2023-12-13 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='email',
        ),
        migrations.RemoveField(
            model_name='client',
            name='phone',
        ),
    ]
# Generated by Django 5.0.1 on 2024-01-05 11:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0014_alter_project_actual_submission'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_wt_mt', models.FloatField()),
                ('monthly_no_sheet', models.FloatField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='official.project')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

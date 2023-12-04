# Generated by Django 4.2.7 on 2023-12-04 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('official', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('assigned_checker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='official.checker')),
                ('assigned_detailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='official.detailer')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='official.client')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2021-08-25 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azure_projects', '0009_auto_20210813_1018'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='download_uri_openvino',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='screenshot',
            field=models.CharField(blank=True, default='', max_length=10000, null=True),
        ),
    ]

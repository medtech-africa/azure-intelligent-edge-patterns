# Generated by Django 3.0.8 on 2020-08-28 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("azure_part_detections", "0004_remove_partdetection_location"),
        ("azure_pd_deploy_status", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeployStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status", models.CharField(max_length=200)),
                ("log", models.CharField(max_length=1000)),
                ("performance", models.CharField(default="{}", max_length=2000)),
                ("need_to_send_notification", models.BooleanField(default=False)),
                (
                    "part_detection",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="azure_part_detections.PartDetection",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(name="TrainingStatus"),
    ]

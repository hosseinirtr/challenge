# Generated by Django 4.1.7 on 2023-12-17 21:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("csv_file_upload", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="status",
            field=models.CharField(
                choices=[("pending", "Pending"), ("sent", "Sent")],
                default="pending",
                max_length=50,
            ),
        ),
    ]
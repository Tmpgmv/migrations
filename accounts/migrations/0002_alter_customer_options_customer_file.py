# Generated by Django 4.1.1 on 2022-10-03 15:35

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='customer',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.user_directory_path),
        ),
    ]
# Generated by Django 4.1.1 on 2022-10-03 15:54

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customer_options_customer_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=accounts.models.UploadTo(a_dir='trololo')),
        ),
    ]

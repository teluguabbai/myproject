# Generated by Django 5.0.6 on 2024-05-20 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_name_details_nam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='nam',
            new_name='name',
        ),
    ]

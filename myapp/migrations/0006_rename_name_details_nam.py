# Generated by Django 5.0.6 on 2024-05-20 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_rename_contents_details'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='name',
            new_name='nam',
        ),
    ]

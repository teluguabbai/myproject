# Generated by Django 5.0.6 on 2024-05-20 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_content_contents'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contents',
            new_name='details',
        ),
    ]

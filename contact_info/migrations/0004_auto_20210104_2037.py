# Generated by Django 3.1.4 on 2021-01-04 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_info', '0003_auto_20210104_1942'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserMessage',
            new_name='UserMessages',
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-08 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0006_auto_20210508_2143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='f_structure',
            old_name='f_type',
            new_name='f_structure',
        ),
    ]

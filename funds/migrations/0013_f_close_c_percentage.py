# Generated by Django 3.1.7 on 2021-10-23 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0012_f_close'),
    ]

    operations = [
        migrations.AddField(
            model_name='f_close',
            name='c_percentage',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=3),
        ),
    ]

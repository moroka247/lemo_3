# Generated by Django 3.1.7 on 2021-06-11 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0008_auto_20210521_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='divest_period_extension_cond',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='final_close_amount',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='final_close_date',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='first_close_amount',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='first_close_date',
        ),
        migrations.RemoveField(
            model_name='fund',
            name='inv_period_extension_cond',
        ),
    ]

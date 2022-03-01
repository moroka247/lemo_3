# Generated by Django 3.1.7 on 2021-11-13 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0013_f_close_c_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='man_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-25 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0002_auto_20210425_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='final_close_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='fund',
            name='first_close_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='fund',
            name='target_commitment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
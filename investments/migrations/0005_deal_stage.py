# Generated by Django 3.1.7 on 2022-04-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investments', '0004_auto_20210620_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='deal_stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=50)),
                ('stage_description', models.TextField(max_length='200')),
            ],
        ),
    ]

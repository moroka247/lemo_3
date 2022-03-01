# Generated by Django 3.1.7 on 2021-05-21 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0007_auto_20210508_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='30')),
                ('code', models.TextField(max_length='4')),
            ],
        ),
        migrations.AddField(
            model_name='fund',
            name='f_currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funds.currency'),
        ),
    ]

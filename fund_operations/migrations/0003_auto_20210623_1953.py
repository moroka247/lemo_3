# Generated by Django 3.1.7 on 2021-06-23 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('funds', '0011_auto_20210619_2204'),
        ('investors', '0002_investor_contact_email'),
        ('fund_operations', '0002_auto_20210623_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='distribution',
            name='distr_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='distribution',
            name='distr_fund',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funds.fund'),
        ),
        migrations.AddField(
            model_name='distribution',
            name='distr_investor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='investors.investor'),
        ),
    ]
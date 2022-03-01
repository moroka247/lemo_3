# Generated by Django 3.1.7 on 2021-06-23 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0002_investor_contact_email'),
        ('funds', '0011_auto_20210619_2204'),
        ('investments', '0004_auto_20210620_1414'),
        ('fund_operations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='capital_call',
            name='call_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='capital_call',
            name='call_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='capital_call',
            name='call_fund',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funds.fund'),
        ),
        migrations.AddField(
            model_name='capital_call',
            name='call_investor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='investors.investor'),
        ),
        migrations.AddField(
            model_name='fund_close',
            name='close_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AddField(
            model_name='fund_close',
            name='close_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fund_close',
            name='close_fund',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funds.fund'),
        ),
        migrations.AddField(
            model_name='fund_close',
            name='close_investor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='investors.investor'),
        ),
        migrations.CreateModel(
            name='disbursement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disb_date', models.DateField()),
                ('disb_fund', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funds.fund')),
                ('disb_investment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='investments.investment')),
            ],
        ),
    ]

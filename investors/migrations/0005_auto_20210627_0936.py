# Generated by Django 3.1.7 on 2021-06-27 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investors', '0004_investor_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_adv_board',
            new_name='adv_board_rep',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_investor',
            new_name='contact_investor',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_inv_comm',
            new_name='inv_comm_rep',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_key_contact',
            new_name='main_contact',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='investor_contact',
            old_name='c_reports',
            new_name='reports',
        ),
    ]
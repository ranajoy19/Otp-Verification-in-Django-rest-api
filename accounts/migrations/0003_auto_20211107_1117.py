# Generated by Django 3.2.9 on 2021-11-07 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_mobile_user_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='otp_token',
            new_name='otp',
        ),
        migrations.AlterField(
            model_name='user',
            name='email_verification_token',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]

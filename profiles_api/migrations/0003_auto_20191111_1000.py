# Generated by Django 2.2.6 on 2019-11-11 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilefeeditem',
            old_name='user_prfile',
            new_name='user_profile',
        ),
    ]
# Generated by Django 3.0 on 2019-12-13 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20191213_2007'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeruser',
            old_name='user',
            new_name='users',
        ),
    ]

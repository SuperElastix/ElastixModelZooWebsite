# Generated by Django 3.0.3 on 2020-09-16 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelzoo', '0009_auto_20200916_1621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model',
            old_name='reviewed',
            new_name='checked',
        ),
    ]

# Generated by Django 3.0.3 on 2020-09-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelzoo', '0013_auto_20200916_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]

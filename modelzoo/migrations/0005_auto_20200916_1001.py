# Generated by Django 3.0.3 on 2020-09-16 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelzoo', '0004_auto_20200916_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='title',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]

# Generated by Django 3.0.3 on 2020-10-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelzoo', '0018_auto_20200921_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='parameter_file10',
        ),
        migrations.RemoveField(
            model_name='model',
            name='reviewed',
        ),
        migrations.AlterField(
            model_name='model',
            name='content',
            field=models.CharField(blank=True, choices=[('Lung', 'Lung'), ('Brain', 'Brain'), ('Prostate', 'Prostate'), ('Chest', 'Chest')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='model',
            name='modality',
            field=models.CharField(blank=True, choices=[('CT', 'CT'), ('Ultrasound', 'Ultrasound'), ('MRI', 'MRI'), ('PET', 'PET')], default='', max_length=15),
        ),
    ]

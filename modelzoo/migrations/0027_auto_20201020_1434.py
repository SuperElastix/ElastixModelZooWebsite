# Generated by Django 3.0.3 on 2020-10-20 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelzoo', '0026_model_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='image1',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image2',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image3',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image4',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image5',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image6',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image7',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image8',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='model',
            name='image9',
            field=models.FileField(blank=True, default='', upload_to='uploads/'),
        ),
    ]

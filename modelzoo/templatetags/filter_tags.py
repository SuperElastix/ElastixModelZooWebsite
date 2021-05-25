from django import template
import os

register = template.Library()

CONTENT_CHOICES = [
    ('Head & Neck', 'Head & Neck'),
    ('Brain', 'Brain'),
    ('Carotid', 'Carotid'),
    ('Chest/Lung', 'Chest/Lung'),
    ('Cardiac', 'Cardiac'),
    ('Abdomen', 'Abdomen'),
    ('Liver', 'Liver'),
    ('Cervix', 'Cervix'),
    ('Prostate','Prostate'),
    ('Pelvis',  'Pelvis'),
    ('Knee', 'Knee'),
    ('Head', 'Head & Neck'),
    ('Neck', 'Head & Neck'),
    ('Chest', 'Chest/Lung'),
    ('Lung', 'Chest/Lung'),
    ('Cervical', 'Cervix'),
    ('Pelvic', 'Pelvis'),
    ]

DIMENSION_CHOICES = [
    ('2D','2D'),
    ('3D', '3D'),
    ('4D','4D'),
    ]

MODALITY_CHOICES = [
    ('CT','CT'),
    ('Ultrasound','Ultrasound'),
    ('MRI','MRI'),
    ('PET', 'PET'),
    ('X-Ray', 'X-Ray'),
    ('MR', 'MRI'),
    ('US', 'Ultrasound')
    ]

@register.simple_tag
def content(x):
    return CONTENT_CHOICES[x][0]

@register.simple_tag
def dimensions(x):
    return DIMENSION_CHOICES[x][0]

@register.simple_tag
def modality(x):
    return MODALITY_CHOICES[x][0]

@register.filter
def filename(value):
    return os.path.basename(value.file.name)

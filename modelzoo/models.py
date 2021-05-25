from django.db import models
from datetime import date
from markdownx.utils import markdownify
from django.urls import reverse
from django.conf import settings
from modelzoo.templatetags.filter_tags import CONTENT_CHOICES, DIMENSION_CHOICES, MODALITY_CHOICES
import nbformat
from nbconvert import HTMLExporter
import re
import io
from django.http import HttpResponse

class Model(models.Model):

    title = models.CharField(max_length = 500, blank=True, default='')
    date = models.DateField(default=date.today)
    content = models.CharField(max_length=15, choices=CONTENT_CHOICES, blank=True, default='')
    modality = models.CharField(max_length=15, choices=MODALITY_CHOICES, blank=True, default='')
    dimensions = models.CharField(max_length=2, choices=DIMENSION_CHOICES, blank=True, default='')
    github = models.CharField(max_length=100, blank=True, default='')
    con_mod_dims = models.CharField(max_length= 200, blank = True, default='')
    slug = models.SlugField(null=True)
    readme = models.FileField(upload_to='uploads/', blank=True, default='')
    ipynb = models.FileField(upload_to='uploads/', blank=True, default='')

    def __str__(self):
        return self.title

    def paper(self):

        found = False
        if self.readme:
            md = open(settings.MEDIA_ROOT + self.readme.name)
        else:
            return

        for line in md.readlines():
            if found and ("." in line or "," in line):
                return line.strip(".-_[]1234567890 ").strip("._-[]1234567890 ")
            elif re.match(r"#+\s*[Pp]ublish",line):
                found = True
            else:
                pass
        return

    def short_description_rm(self):
        found = False
        if self.readme:
            md = open(settings.MEDIA_ROOT + self.readme.name)
        else:
            return
        for line in md.readlines():
            if found and line != "\n":
                return line
            elif re.match(r"#+\s*[Rr]egistration [Dd]escription", line):
                found = True

        md.seek(0)

        for line in md.readlines():
            if re.match("[A-Z]", line) and len(line)>20:
                description = line + md.readline() + md.readline() + md.readline() + md.readline()
                return description[:100] + '...'
        md.seek(0)
        description = ' '.join(md.readlines()[2:])
        return description[:100] + '...'

    def formatted_markdown(self):
        if self.readme:
            return markdownify(open(settings.MEDIA_ROOT + self.readme.name).read())
        elif self.readme_txt:
            return markdownify(self.readme_txt)
        else:
            return

    def description_rm(self):
        if self.readme:
            md = open(settings.MEDIA_ROOT + self.readme.name)
        elif self.readme_txt:
            md = io.StringIO(self.readme_txt)
        else:
            return
        return md.readlines()

    def formatted_ipynb(self):
        if self.ipynb:
            notebook = nbformat.reads(open(settings.MEDIA_ROOT + self.ipynb.name).read(), as_version=4)
            html_exporter = HTMLExporter()
            html_exporter.template_name = 'classic'
            (body, resources) = html_exporter.from_notebook_node(notebook)
            return body
        else:
            return

    def get_absolute_url(self):
        return reverse(
            "modelzoo:detail",
            kwargs={
                "slug": self.slug
            }
        )

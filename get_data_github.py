import os
import requests
from django.db import models

os.environ.setdefault('DJANGO_SETTINGS_MODULE','ModelZooElastix.settings')
import django

django.setup()
from modelzoo.models import Model
from django.core.files import File
from django.utils.text import slugify
from modelzoo.templatetags.filter_tags import CONTENT_CHOICES, DIMENSION_CHOICES, MODALITY_CHOICES
import re

git_clone = "git clone https://github.com/SuperElastix/ElastixModelZoo.git"
git_pull = "cd ElastixModelZoo && git fetch && git reset --hard origin/master"

repo =  "ElastixModelZoo/models"
upload_folder = "ModelZooElastix/media/uploads"

def github_update():
    if os.path.exists("ElastixModelZoo"):
        os.system(git_pull)
    else:
        os.system(git_clone)

def make_models():
    Model.objects.all().delete()
    for root, dirs, files in os.walk(upload_folder):
        for f in files:
            os.unlink(os.path.join(root, f))
    for dir in os.listdir(repo):
        directory = os.path.join(repo, dir)
        d, created = Model.objects.update_or_create(title=dir)
        github_link = "https://github.com/SuperElastix/ElastixModelZoo/tree/master/models/" + dir
        d.github = github_link
        d.slug = slugify(dir)
        # p = 0
        images = []
        md = ''

        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".md"):
                    con_mod_dims = ''
                    md = filename
                    reopen = open(os.path.join(directory, filename), "rb")
                    last_line_str = str(reopen.read()).lower()
                    for content in CONTENT_CHOICES:
                        if bool(re.search(r'\b'+content[0].lower()+r'\b', last_line_str)) and not bool(re.search(content[1], con_mod_dims)):
                            d.content = content[1]
                            con_mod_dims += content[1] + ' '
                            d.save()
                    for dimension in DIMENSION_CHOICES:
                        if bool(re.search(r'\b'+dimension[0].lower()+r'\b', last_line_str)) and not bool(re.search(dimension[1], con_mod_dims)):
                            d.dimensions = dimension[1]
                            con_mod_dims += dimension[1] + ' '
                            d.save()
                    for modality in MODALITY_CHOICES:
                        if bool(re.search(r'\b'+modality[0].lower()+r'\b', last_line_str)) and not bool(re.search(modality[1], con_mod_dims)):
                            d.modality = modality[1]
                            con_mod_dims += modality[1] + ' '
                            d.save()
                    d.con_mod_dims = con_mod_dims

                    match = re.findall(r'\[\d\]', last_line_str)
                    nr_of_refs = 1
                    if match:
                        int_str = match[-1].strip(' []')
                        nr_of_refs = int(int_str) + 1

                    d.save()
                    reopen.close()

                elif filename.endswith(".ipynb"):
                    nbopen = open(os.path.join(directory, filename), "rb")
                    nb = File(nbopen)
                    d.ipynb.save(filename, nb, save=True)
                    nbopen.close()

                elif filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".gif"):
                    images.append(filename)

        # Replace local github references to github webreference.
        mdopen = open(os.path.join(directory, md), 'rt')
        mdopen_data = mdopen.read()

        for i,filename in enumerate(images):
            i += nr_of_refs
            mdopen_data = mdopen_data.replace('({})'.format(filename), '[{}]'.format(i))

        mdopen_data = re.sub(r'#+\s*[Rr]egistration [Ss]ettings', '### Registration Settings \n For parameter files see [the Elastix Model Zoo repository]({}) on GitHub.'.format(github_link), mdopen_data)
        mdopen.close()
        mdopen = open(os.path.join(directory, md), 'wt')
        mdopen.write(mdopen_data)

        for i, filename in enumerate(images):
            if i==0:
                mdopen.write('\n')
            i += nr_of_refs
            mdopen.write('[{}]: https://github.com/SuperElastix/ElastixModelZoo/raw/master/models/{}/{} \n'.format(i, dir, filename))

        mdopen.close()
        mdopen = open(os.path.join(directory, md), "rb")

        rm = File(mdopen)
        d.readme.save(md, rm, save=True)


if __name__ == "__main__":
    github_update()
    make_models()

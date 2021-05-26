# Elastix Model Zoo Website

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/SuperElastix/elastix/raw/master/LICENSE)
[![Model Zoo](https://img.shields.io/badge/open-Model%20Zoo-blue.svg)](https://elastix.lumc.nl/modelzoo/)

Welcome to the elastix model zoo django website.

Note: This is not the repository where you should upload your parameter files,
for this checkout the [model zoo] repository.

The elastix model zoo is a dynamic website that uses github's version control
to monitor it's content contributions. The website is built with django and is hosted at:
https://elastix.lumc.nl/modelzoo

![Screenshot 2021-05-26 at 14 52 26](https://user-images.githubusercontent.com/33719474/119662811-1717a580-be32-11eb-842a-25c48432e9fb.png)


The elastix model zoo repository is a submodule of this website repository and
has to be cloned separately. In order to do so, run the following after a clone of this repository:

    cd ModelZooElastix/ElastixModelZoo

    git submodule init

    git submodule update

## More information about elastix ##

More information about the elastix algorithm, including an extensive manual can be found on the [wiki](https://github.com/SuperElastix/elastix/wiki)

Interactive tutorials are available in [Jupyter notebooks](https://mybinder.org/v2/gh/InsightSoftwareConsortium/ITKElastix/master?urlpath=lab/tree/examples%2FITK_Example01_SimpleRegistration.ipynb).

You can also subscribe to the [mailing list](https://groups.google.com/forum/#!forum/elastix-imageregistration) for questions.


[model zoo]: https://github.com/SuperElastix/ElastixModelZoo

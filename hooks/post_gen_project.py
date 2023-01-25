#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))
def remCondaFile(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY,'conda-recipe', filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if '{{ cookiecutter.use_conda }}' == 'n':
        [remCondaFile(f) for f in ('bld.bat','build.sh','conda_build_config.yaml','meta.yaml')]
        os.rmdir(os.path.join(PROJECT_DIRECTORY,'conda-recipe'))

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

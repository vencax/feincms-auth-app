#!/usr/bin/env python
from setuptools import setup, find_packages
import os

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

description = '''
django-social-auth-app utilizes django-social-auth and make it easy to
integrate into existing project. It also solves login and logout.
Some templates are added.
'''

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description

setup(name='django-social-auth-app',
    version='',
    description=description,
    license='BSD',
    url='https://github.com/vencax/django-social-auth-app',
    author='vencax',
    author_email='vencax@centrum.cz',
    packages=find_packages(),
    install_requires=[
        'django-social-auth'
    ],
    keywords="django social auth login util",
    include_package_data=True,
)

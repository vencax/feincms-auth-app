#!/usr/bin/env python
from setuptools import setup, find_packages
import os

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README')

description = '''
django-social-auth-app utilizes django-registration and
django-social-auth and handle all user related actions within
single application. Intended to use with feincms.
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

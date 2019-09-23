# /usr/bin/python3
import codecs
import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='djcms-custom-menu',
    version='1.0.5',
    description='An extension for Django CMS that allows you to create and edit multiple menus like Wordpress. This is compatible for Python 3.6, Django 2.1.9, django-cms 3.6.0',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Abdullah Al Arafat Bipul',
    author_email='imbipul9@gmail.com',
    license='MIT',
    url='https://github.com/imbipul/djcms-custom-menu',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=2.1.9',
        'django-classy-tags',
        'django-cms>=3.6.0',
        'jsonfield>=1.0.0',
        'django-autoslug>=1.7.2',
    ],
    package_data={
        'readme': ['README.rst'],
        'license': ['LICENSE']
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

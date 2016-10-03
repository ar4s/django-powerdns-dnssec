#!/usr/bin/env python

import json
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages


with open(
    os.path.join(os.path.dirname(__file__), 'README.rst'),
    encoding='utf-8'
) as f:
    long_description = f.read()

with open('version.json') as f:
    version = '.'.join(str(part) for part in json.load(f))

with open('requirements/base.txt') as f:
    requirements = f.readlines()

setup(
    name = 'django-powerdns-dnssec',
    version = version,
    url = 'http://bitbucket.org/ambv/django-powerdns/',
    license = 'BSD',
    description = 'PowerDNS administration app for Django',
    long_description = long_description,
    author = 'Peter Nixon, Łukasz Langa, pylabs Team',
    author_email = 'pylabs@allegro.pl',
    packages = [p for p in find_packages() if not p.startswith('example')],
    include_package_data = True,
    platforms = 'any',
    entry_points={
        'console_scripts': [
            'dnsaas = dnsaas.__main__:prod',
            'dev_dnsaas = dnsaas.__main__:dev',
            'test_dnsaas = dnsaas.__main__:test',
            'local_dnsaas = dnsaas.__main__:local',
        ],
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Telecommunications Industry',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: Name Service (DNS)',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = requirements,
    zip_safe = False,  # if only because of the readme file
)

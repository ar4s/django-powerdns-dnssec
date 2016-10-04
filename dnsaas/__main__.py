#!/usr/bin/env python
import os
import sys


def main(settings_module='dnsaas.settings', force=False):
    if force:
        os.environ['DJANGO_SETTINGS_MODULE'] = settings_module
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


def dev():
    main('dnsaas.settings.dev')


def test():
    # test only with test settings, not local (or any set by environment
    # variable DJANGO_SETTINGS_MODULE) - especially usefull in vagrant, when
    # default DJANGO_SETTINGS_MODULE is overwrited in .profile
    main('dnsaas.settings.test', force=True)


def prod():
    main('dnsaas.settings.prod')


def local():
    try:
        main('dnsaas.settings.local')
    except ImportError:
        print('Copy file settings/local.py.tmpl to settings/local.py and customize it.')  # noqa


if __name__ == '__main__':
    main('dnsaas.settings')

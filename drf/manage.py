#!/usr/bin/env python
import os
import sys

from django.core.management.commands.runserver import Command as Runserver
from django.urls import get_urlconf, get_resolver, URLPattern, URLResolver
if __name__ == "__main__":
    Runserver.default_addr = '0.0.0.0'
    Runserver.default_port = '8081'

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    print(sys.argv)
    execute_from_command_line(sys.argv)


    def get_all_url(resolver=None, pre='/'):
        if resolver is None:
            resolver = get_resolver()
        for r in resolver.url_patterns:
            if isinstance(r, URLPattern):
                if '<pk>' in str(r.pattern):
                    continue
                yield pre + str(r.pattern).replace('^', '').replace('$', ''), r.name
            if isinstance(r, URLResolver):
                yield from get_all_url(r, pre + str(r.pattern))


    for url, name in get_all_url():
        print("url='{}'  name='{}'".format(url, name))
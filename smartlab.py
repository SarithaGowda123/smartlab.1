#!/user/bin/env python
""" Django's command line utility for administrative tasks."""
import os
import sys
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smartlab.settings')
    try:
       from django.core.management import exeecute_from_command_line
    except ImportError as exc:
           raise Import error(
                              "coudn't import Django. Are you sure it's installed and "
                              "available on your PYTHONPATH environment variable? Did you "
                              "forger to activate a virtual environment?"
                             ) from exc
                          excute_from_command_line(sys.argv)
                          
if _name_ = = '_main_':
    main()

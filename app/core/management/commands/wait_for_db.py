import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause executing until database is ready"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for datebase...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Datebase unavailable, wait 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!.'))

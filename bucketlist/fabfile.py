import os

from fabric.api import local, task
from fabric.decorators import runs_once

BASE_DIR = os.path.sep.join((os.path.dirname(__file__), ''))

@task
@runs_once
def runserver():
    """
    Runs the local Django server
    """
    local('open "http://localhost:8000" && python3 manage.py runserver')

#!/usr/bin/python3
"""
returns the status of the app_views object at route /status
"""

from api.v1 import views
from models import storage
from json import dumps
from collections import defaultdict


@views.app_views.route("/status")
def status():
    return dumps({"status": "OK"})


@views.app_views.route("/stats")
def stats():
    """Get number of objects indexed by type"""
    numbers = defaultdict(lambda: 0)
    for value in storage.all().values():
        numbers[str(type(value))] += 1
    return dumps(numbers)

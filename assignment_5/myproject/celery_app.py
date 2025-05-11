from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Create the Celery app instance
app = Celery("myproject")

# Load configuration from Django settings, using CELERY_ prefix
app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks from all registered Django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

# Optional, already in your settings — but valid to keep here
app.conf.result_backend = "redis://localhost:6379/0"

from __future__ import absolute_import, unicode_literals
import os
from assignment_5.myproject.celery_app import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
  # necessary to set the settings module for Django
# This will make sure the app is always imported when Django starts so that shared_task will use this app.
# This is important for the task to be registered with the Django app.


app = Celery("myproject")  # project name
app.conf.enable_utc = False

app.config_from_object("django.conf:settings", namespace="CELERY")


app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


app.conf.result_backend = "redis://localhost:6379/0"  # ✅



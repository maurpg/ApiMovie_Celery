import os
from celery import Celery
from celery.schedules import crontab


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ApiMovies.settings')
app = Celery('ApiMovies' , broker='amqp://guest:guest@localhost:5672//' , backend='django-db')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
"""
app.conf.beat_schedule = {
    'check_table_movie':{
        'task':'Movie.tasks.check_table_movies_suggest',
        'schedule':crontab(minute = '*/1'),
        'args':()
    }
}
"""

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
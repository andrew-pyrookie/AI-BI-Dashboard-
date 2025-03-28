import os
from celery import Celery

# Set the default Django settings module for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BI_board.settings')

# Create a Celery instance and configure it using the settings from Django
app = Celery('BI_board')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps (e.g., 'apps.data_ingestion')
app.autodiscover_tasks()
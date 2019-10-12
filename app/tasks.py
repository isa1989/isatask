
from celery.decorators import task
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from Todo.celery import app as celery_app
from .emails import send_feedback_email
from celery.task.schedules import crontab
from .models import *
from datetime import datetime, date, timedelta
from django.utils import timezone
from django.http import HttpRequest

from django.utils.timezone import timedelta
from django.core.mail import send_mail

logger = get_task_logger(__name__)



@task(name="task__expired")
def endtime_date(*args):
    carriers = Task.objects.all()
    for carrier in carriers:
        from django.utils import timezone
        now = timezone.now()
        if carrier.end_time <= now + timedelta(minutes=10) and carrier.end_time > now + timedelta(minutes=9) :
            print("isleyirrrrrr")
            from django.core.mail import send_mail
            email = carrier.user.email
            send_mail(
            'Subject here celery',
            'Tapşırığın bitməyinə 10 dəqiqə qalıb.',
            'isaramazanov89@gmail.com',
            [email]
              )

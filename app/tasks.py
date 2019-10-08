from celery.decorators import task
from celery.task import periodic_task
from celery.utils.log import get_task_logger
from Todo.celery import app as celery_app
from .emails import send_feedback_email
from celery.task.schedules import crontab
from .models import *
from datetime import datetime, date, timedelta
from django.utils import timezone

from django.utils.timezone import timedelta

logger = get_task_logger(__name__)


@task(name="send_feedback_email_task")
def send_feedback_email_task(email, message):
    """sends an email when feedback form is filled successfully"""
    logger.info("Sent feedback email")
    return send_feedback_email(email, message)

@celery_app.task(name="foobar.sample_task")
def sample_task(value):
    print(value)

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task", ignore_result=True)

def some_task():
   logger.info("bura islekdir")

@task(name="insurance_expired")
def endtime_date(*args):
    carriers = Task.objects.all()
    for carrier in carriers:
        from django.utils import timezone
        now = timezone.now()
        if carrier.end_time <= now + timedelta(minutes=2) and carrier.end_time > now :
           # logger.info("model isledi")
            print("isleyirrrrrr")
        else:
            print("islemedi")
 #   logger.info("ssssssss")
 #   print("ssssssssssss")
   
 
@periodic_task(run_every=timedelta(seconds=5))
def print_hello():
    print('Hello World!')

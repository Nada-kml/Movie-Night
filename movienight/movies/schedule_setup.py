from django_celery_beat.models import PeriodicTask
from django_celery_beat.models import IntervalSchedule
def schedule_setup():
    day_schedule, created = IntervalSchedule.objects.get_or_create(period=IntervalSchedule.MINUTES, every=1)
    pt = PeriodicTask.objects.create(name="Notification of start", interval=day_schedule, task="movies.tasks.notify_of_starting_soon")

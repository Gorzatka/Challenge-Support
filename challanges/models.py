from django.db import models
from django.utils import timezone


class Challenge(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    challenge_start_date = models.DateTimeField(default=timezone.now)
    challenge_end_date = models.DateTimeField(default=timezone.now)
    challenge_current_date = models.DateTimeField(default=timezone.now)
    In_progress = 'In progress'
    Complete = 'Complete'
    status_choices = (
        (In_progress, 'In progress'),
        (Complete, 'Complete'),

         )
    challenge_status = models.CharField(max_length=11, choices=status_choices, default=In_progress)
    #days_left = models.
    #money_saved
    #calories_saved
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.challenge_status = Challenge.Complete
        self.save()

    def __str__(self):
        return self.title


class Story(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=500)
    published_date = models.DateTimeField(blank=True, null=True)








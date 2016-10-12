from django.db import models
from django.utils import timezone


class Challenge(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    challenge_start_date = models.DateTimeField(default=timezone.now)
    challenge_end_date = models.DateTimeField
    #money_saved
    #calories_saved
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

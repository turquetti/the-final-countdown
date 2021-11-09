from django.db import models
from django.db.models.fields import URLField

class CountdownMusic(models.Model):
    music_url = models.URLField("Music URL", max_length=200)
    posting_date = models.DateField("Posting Date")
    end_date = models.DateField("End Date")


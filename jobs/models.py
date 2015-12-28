from django.db import models

# Create your models here.


class Job(models.Model):

    """Docstring for . """
    sch_name = models.CharField(max_length=200)
    subj = models.CharField(max_length=200)
    jmessage = models.CharField(max_length=500)

    def __str__(self):
        return self.sch_name

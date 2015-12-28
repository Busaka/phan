from django.db import models

# Create your models here.


class School(models.Model):
    """Docstring for Schools. """
    school_name = models.CharField(max_length=200)
    description = models.TextField()
    school_photo = models.ImageField(upload_to='school_photos')
    published = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.school_name


# class Job(models.Model):

#     """Docstring for . """
#     school_name = models.CharField(max_length=200)
#     subject = models.CharField(max_length=200)
#     message = models.TextField()

#     def __str__(self):
#         return self.school_name

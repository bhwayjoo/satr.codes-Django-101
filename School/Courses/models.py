from django.db import models

# Create your models here.
class Fields (models.Model):
    CourseName=models.CharField(max_length=50,help_text =('Cours'))
    CourseNumber=models.IntegerField(help_text =('Course Number represents the Course ID'))

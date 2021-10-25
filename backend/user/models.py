from django.db import models

# Create your models here.
class User(models.Model):
    YEAR_IN_SCHOOL_CHOICES = [('F', 'Faculty'), ('UG', 'Undergraduate'), ('G', 'Graduate')]
    RECOMMEND_CHOICES = [('Y', 'Yes'), ('N', 'No')]

    name = models.TextField(primary_key=True)
    age = models.IntegerField()
    recommended = models.CharField(max_length=1, choices=RECOMMEND_CHOICES)
    status = models.CharField(max_length=2, choices=YEAR_IN_SCHOOL_CHOICES)
    feedback = models.TextField()

    def _str_(self):
        return self.name
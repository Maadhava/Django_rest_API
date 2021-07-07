from django.db import models

# Create your models here.
class students(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    stud_id=models.IntegerField()

    def __str__(self):
        return self.firstname
from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    total_marks = models.IntegerField()
    # Add other fields such as YearofStudy, course, age, approx_height, approx_weight

    def __str__(self):
        return self.name
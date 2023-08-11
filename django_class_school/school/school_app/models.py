from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.
class Person(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    courses = models.ManyToManyField('course', blank=True)
    
    class Meta:
        verbose_name_plural = "people"
        
class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()
    
    class Meta:
        unique_together =("name","year",)
        
class Grade(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    grade= models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0),MaxValueValidator(100)]
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
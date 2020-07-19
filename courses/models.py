from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, form):
        errors = {}
        if len(form['name']) < 5:
            errors['name'] = 'Name of course should be at least 5 characters'
        if len(form['description']) < 15:
            errors['description'] = 'Description should be at least 15 characters'
        return errors

class Course (models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = CourseManager()
from django.db import models

# Create your models here.
class Function(models.Model):
    function_name = models.CharField(max_length=255)

    def __str__(self):
        return self.function_name


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    function = models.ForeignKey(Function, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_leader = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.project_name}'

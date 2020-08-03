from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    status = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    status = models.CharField(max_length=10, blank=True)
    created_date = models.DateTimeField(blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    fk_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Faculty")

    def __str__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    uc = models.IntegerField()
    semester = models.IntegerField()
    tipo = models.CharField(max_length=9)
    ht = models.FloatField(default=0)
    hp =  models.FloatField(default=0, null=True, blank=True)
    hl = models.FloatField(default=0, null=True, blank=True)
    created_date = models.DateTimeField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    fk_school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="School")

    def __str__(self):
        return self.name


class Person(models.Model):
    dni = models.CharField(max_length=8)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    created_date = models.DateTimeField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
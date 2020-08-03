from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    created_date = models.DateTimeField()
    deleted_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

class School(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    status = models.CharField(max_length=10)
    created_date = models.DateTimeField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    fk_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name="Faculty")

    def __str__(self):
        return self.name
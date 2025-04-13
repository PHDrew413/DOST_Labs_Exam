from django.db import models

class Labs(models.Model):
    lab_name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    instructor = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.lab_name

from django.db import models

class Practice(models.Model):
    image = models.FileField(upload_to="practices")
    name = models.CharField(max_length=255)


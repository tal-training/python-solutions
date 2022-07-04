import uuid
from django.db import models
# Create your models here.

class FlightModel(models.Model):
    company=models.CharField(max_length=100, default="default")
    date=models.CharField(max_length=100, default="default")
    city=models.CharField(max_length=100, default="default")
    country=models.CharField(max_length=100, default="default")
    status=models.CharField(max_length=100, default="default")
    key=models.UUIDField(default=uuid.uuid4, primary_key=True)


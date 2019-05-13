from django.db import models

# Create your models here.
import datetime
# Create your models here.
class Book1(models.Model):
    name=models.CharField(max_length=50)
    publication_date=models.DateField(default=datetime.date.today())

    class Meta:
        db_table="Book1"
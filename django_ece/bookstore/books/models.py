from django.db import models

# Create your models here.
from django.db import models

class Book(models.model):
    title = models.charField(max_length=100)
    author = models.charField(max_length=100)
    published_date = models.DataField()

    def __str__(self):
        return self.title


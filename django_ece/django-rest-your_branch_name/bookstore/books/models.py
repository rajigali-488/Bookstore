from django.db import models
class Book(models.Model):
      title = models.charField(max_length=100)
      author = models.charField(max_length=100)
      published_Date = models.DataField()
      def __str__(self):
            return self.title

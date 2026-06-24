from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title

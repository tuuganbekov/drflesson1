from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True``)
    image = models.ImageField(upload_to="movies/")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

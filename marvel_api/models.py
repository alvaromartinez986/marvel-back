from django.db import models

class Character(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    imgUrl = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Comic(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    characters = models.ManyToManyField(Character, related_name='comics')
    description = models.TextField()
    imgUrl = models.URLField()

class ApiStatus(models.Model):
    data_loaded = models.BooleanField(default=False)



    def __str__(self):
        return self.title

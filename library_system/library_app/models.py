from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class TestResult(models.Model):
    test_name = models.CharField(max_length=100)
    score = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.test_name} - {self.score}"

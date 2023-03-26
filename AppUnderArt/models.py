from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=20)
    book_author = models.CharField(max_length=20)
    book_edition_year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2023)])
    book_image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f"{self.book_name}, escrito por {self.book_author} ({self.book_edition_year})"


class Movie(models.Model):
    movie_name = models.CharField(max_length=20)
    movie_director = models.CharField(max_length=20)
    movie_release_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2023)])
    movie_image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f"{self.movie_name}, dirigida por {self.movie_director} ({self.movie_release_year})"


class ArtWork(models.Model):
    piece_name = models.CharField(max_length=20)
    piece_author = models.CharField(max_length=20)
    piece_creation_year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2023)])
    piece_image = models.ImageField(null=True, blank=True, upload_to="media/")

    def __str__(self):
        return f"{self.piece_name}, hecho por {self.piece_author} ({self.piece_creation_year})"


class Song(models.Model):
    song_name = models.CharField(max_length=10)
    song_author = models.CharField(max_length=20)
    song_creation_year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2023)])
    song_image = models.ImageField(null=True, blank=True, upload_to="media/artWork")

    def __str__(self):
        return f"{self.song_name}, autoria  {self.song_author} ({self.song_creation_year})"

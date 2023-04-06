from datetime import timezone

from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User
from django.template.backends import django
from django.urls import reverse


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


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def publish(self):
        self.published_date = django.utils.timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

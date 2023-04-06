from django import forms
from django.contrib.contenttypes.models import ContentType
from .models import Book, Movie, ArtWork, Comment, Post


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'book_author', 'book_edition_year', 'book_image')


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_director', 'movie_release_year', 'movie_image']


class ArtWorkForm(forms.ModelForm):
    class Meta:
        model = ArtWork
        fields = ['piece_name', 'piece_author', 'piece_creation_year', 'piece_image']


class ContentTypeForm(forms.Form):
    CONTENT_CHOICES = [
        ('Book', 'Libro'),
        ('ArtWork', 'Obra de arte'),
        ('Movie', 'Pelicula'),
    ]
    content_type = forms.ChoiceField(choices=CONTENT_CHOICES, widget=forms.RadioSelect)


class SearchForm(forms.Form):
    name = forms.CharField(max_length=40)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

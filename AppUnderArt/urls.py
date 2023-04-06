from django.urls import path
from AppUnderArt import views
from AppUnderArt.static.views import create_content, about
from AppUnderArt.viewsBook import *
from AppUnderArt.viewsMovie import *
from AppUnderArt.viewsArtWork import *


urlpatterns = [
    path('', home, name='AppUnderArtHome'),
    path('underArt/about', about, name='AppUnderAbout'),

    path('underArt/createContent', create_content, name="AppUnderArtCreateContent"),
    path('underArt/createBook', create_book, name="AppUnderArtCreateBook"),
    path('underArt/createMovie', create_movie, name="AppUnderArtCreateMovie"),
    path('underArt/createArtWork', create_artwork, name="AppUnderArtCreateArtWork"),
    path('underArt', books, name="AppUnderArtBooks"),
    path('underArt/searchBook', search_book, name="AppUnderArtSearchBooks"),
    path('underArt/editBook/<book_name>', edit_book, name="AppUnderArtEditBook"),
    path('underArt/deleteBook/<book_name>', delete_book, name="AppUnderArtDeleteBook"),

    path('underArt/movies', movies, name="AppUnderArtMovies"),
    path('underArt/searchMovie', search_movie, name="AppUnderArtSearchMovies"),
    path('underArt/editMovie/<movie_name>', edit_movie, name="AppUnderArtEditMovie"),
    path('underArt/deleteMovie/<movie_name>', delete_movie, name="AppUnderArtDeleteMovie"),

    path('underArt/artworks', artworks, name="AppUnderArtArtWorks"),
    path('underArt/searchartWorks', search_artwork, name="AppUnderArtSearchArtWorks"),
    path('underArt/editArtwork/<piece_name>', edit_artwork, name="AppUnderArtEditArtWrok"),
    path('underArt/deleteArtwork/<piece_name>', delete_artwork, name="AppUnderArtDeleteArtWork"),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

]

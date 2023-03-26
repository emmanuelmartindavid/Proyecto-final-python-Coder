from django.http import HttpResponse
from django.urls import path

from AppUnderArt.forms import ContentTypeForm
from AppUnderArt.viewsBook import *
from AppUnderArt.viewsMovie import *
from AppUnderArt.viewsArtWork import *


def create_content(request):
    if request.method == 'POST':
        content_type = request.POST.get('content_type')

        return redirect(f"AppUnderArtCreate{content_type}")

    context = {
        "form": ContentTypeForm(),
        "title": "Crear contenido",
        "send": "Crear",
    }
    return render(request, "AppUnderArt/creation.html", context=context)


urlpatterns = [
    path('', home, name='AppUnderArtHome'),
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
]

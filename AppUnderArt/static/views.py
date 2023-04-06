from django.shortcuts import redirect, render

from AppUnderArt.forms import ContentTypeForm


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


def about(request):
    return render(request, "AppUnderArt/about.html")

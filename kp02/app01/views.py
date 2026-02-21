from django.http import HttpResponse


def response(request):
    return HttpResponse("Hello World!")


def response2(request):
    return HttpResponse(
        "<h1>Text Page</h1>"
        "<p>Name and surname: Stepan Potiienko</p>"
        "<p>This is the /text/ page for practical work #2.</p>"
    )

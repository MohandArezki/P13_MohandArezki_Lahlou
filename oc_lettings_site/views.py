from django.shortcuts import render
import logging
from django.http import HttpRequest


logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie quam lobortis leo
# consectetur ullamcorper non id est. Praesent dictum, nulla eget feugiat sagittis,
# sem mi convallis eros, vitae dapibus nisi lorem dapibus sem.
# Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis
# enim cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    View function for the index page.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response for the index page.
    """
    logger.info("Displaying home page.")
    return render(request, 'index.html')


def handler404(request: HttpRequest, exception: Exception):
    """
    View function for handling 404 errors.

    Parameters:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception object representing the 404 error.

    Returns:
        HttpResponse: Rendered response for the 404 error page.
    """
    return render(request, '404.html', status=404)


def handler500(request: HttpRequest):
    """
    View function for handling 500 errors.

    Parameters:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered response for the 500 error page.
    """
    return render(request, '500.html', status=500)

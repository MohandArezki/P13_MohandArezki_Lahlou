from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import index, handler404, handler500


class ViewsTestCase(TestCase):
    def test_index_view(self):
        """
        Test the index view.
        """
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('index.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_handler404_view(self):
        """
        Test the handler404 view.
        """
        request = HttpRequest()
        response = handler404(request, Exception())
        self.assertEqual(response.status_code, 404)
        expected_html = render_to_string('404.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_handler500_view(self):
        """
        Test the handler500 view.
        """
        request = HttpRequest()
        response = handler500(request)
        self.assertEqual(response.status_code, 500)
        expected_html = render_to_string('500.html')
        self.assertEqual(response.content.decode(), expected_html)

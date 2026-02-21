from django.test import SimpleTestCase


class App01ViewsTests(SimpleTestCase):
    def test_home_page_returns_200_and_expected_text(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello World!")

    def test_text_page_returns_200_and_contains_name(self):
        response = self.client.get("/text/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Stepan Potiienko")

from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Початкова сторінка</h1>")


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>Сторінка about</h1>")


class TextPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/text/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("text"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("text"))
        self.assertTemplateUsed(response, "text.html")

    def test_template_content(self):
        response = self.client.get(reverse("text"))
        self.assertContains(response, "<h1>Text Page</h1>")


class ResumePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/resume/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("resume"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("resume"))
        self.assertTemplateUsed(response, "resume.html")

    def test_template_content(self):
        response = self.client.get(reverse("resume"))
        self.assertContains(response, "<h1>Stepan Potiienko - Resume</h1>")


class NegativeTest(SimpleTestCase):
    def test_home_returns_status_300(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 300)

from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post1 = Post.objects.create(text="Python and Django developer with 2 years of experience.")
        cls.post2 = Post.objects.create(text="Skills: Python, Django, HTML, CSS, Git.")
        cls.post3 = Post.objects.create(text="Contact: spotiienko@icloud.com")
        cls.post4 = Post.objects.create(text="GitHub: https://github.com/StepanPotiienko/")

    def test_model_content(self):
        self.assertEqual(self.post1.text, "Python and Django developer with 2 years of experience.")

    def test_url_exists(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_used(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_homepage_content_matches_db(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post2.text)
        self.assertContains(response, self.post3.text)
        self.assertContains(response, self.post4.text)

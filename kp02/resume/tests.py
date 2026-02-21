from django.test import SimpleTestCase


class ResumeViewsTests(SimpleTestCase):
    def test_resume_page_returns_200_and_contains_title(self):
        response = self.client.get("/resume/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Stepan Potiienko - Resume")

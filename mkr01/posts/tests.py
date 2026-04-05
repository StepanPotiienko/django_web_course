from django.test import TestCase
from django.urls import reverse
from datetime import date

from .models import Post


class HomeViewTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_home_page_displays_post_text(self):
        Post.objects.create(text="Recovered post")
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Recovered post")

    def test_home_page_displays_table_headers(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Text")
        self.assertContains(response, "Date")
        self.assertContains(response, "Temperature")
        self.assertContains(response, "Pressure")
        self.assertContains(response, "Wind speed")
        self.assertContains(response, "Precipitation probability")

    def test_home_page_displays_all_measurement_fields(self):
        Post.objects.create(
            text="Kyiv center",
            date=date(2026, 4, 5),
            temperature=14.5,
            pressure=1009.2,
            wind_speed=5.3,
            precipitation_probability=0.4,
        )
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Kyiv center")
        self.assertContains(response, "April 5, 2026")
        self.assertContains(response, "14.5")
        self.assertContains(response, "1009.2")
        self.assertContains(response, "5.3")
        self.assertContains(response, "0.4")

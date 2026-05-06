from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Measurement

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = get_user_model().objects.create_user(username="testuser", password="password")
        cls.post = Post.objects.create(title="Test Post", body="Test Body", author=user)

    def test_blog_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "home.html")

    def test_blog_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Body")
        self.assertTemplateUsed(response, "post_detail.html")

class WeatherTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.measurement = Measurement.objects.create(
            text="Test Weather", 
            temperature=15.0,
            pressure=1010.0,
            wind_speed=5.0,
            precipitation_probability=0.2
        )

    def test_weather_listview(self):
        response = self.client.get(reverse("weather_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Weather")
        self.assertTemplateUsed(response, "weather_list.html")

    def test_weather_detailview(self):
        response = self.client.get(reverse("measurement_detail", kwargs={"pk": self.measurement.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Weather")
        self.assertTemplateUsed(response, "measurement_detail.html")

    def test_measurement_createview(self):
        response = self.client.post(
            reverse("measurement_new"),
            {
                "text": "New Weather Entry",
                "temperature": 20.0,
                "pressure": 1015.0,
                "wind_speed": 10.0,
                "precipitation_probability": 0.5,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Measurement.objects.last().text, "New Weather Entry")

    def test_measurement_updateview(self):
        response = self.client.post(
            reverse("measurement_edit", kwargs={"pk": self.measurement.pk}),
            {
                "text": "Updated Weather",
                "temperature": self.measurement.temperature,
                "pressure": self.measurement.pressure,
                "wind_speed": self.measurement.wind_speed,
                "precipitation_probability": self.measurement.precipitation_probability,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.measurement.refresh_from_db()
        self.assertEqual(self.measurement.text, "Updated Weather")

    def test_measurement_deleteview(self):
        response = self.client.post(reverse("measurement_delete", kwargs={"pk": self.measurement.pk}))
        self.assertEqual(response.status_code, 302)

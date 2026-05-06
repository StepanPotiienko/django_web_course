from django.urls import path
from .views import (
    BlogListView, BlogDetailView,
    WeatherListView, WeatherDetailView,
    MeasurementCreateView, MeasurementUpdateView, MeasurementDeleteView
)

urlpatterns = [
    # Blog
    path("", BlogListView.as_view(), name="home"),
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),

    # Weather
    path("weather/", WeatherListView.as_view(), name="weather_list"),
    path("weather/<int:pk>/", WeatherDetailView.as_view(), name="measurement_detail"),
    path("weather/new/", MeasurementCreateView.as_view(), name="measurement_new"),
    path("weather/<int:pk>/edit/", MeasurementUpdateView.as_view(), name="measurement_edit"),
    path("weather/<int:pk>/delete/", MeasurementDeleteView.as_view(), name="measurement_delete"),
]

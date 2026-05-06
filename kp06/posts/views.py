from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Measurement

# Blog Views
class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "post_list"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

# Weather Views
class WeatherListView(ListView):
    model = Measurement
    template_name = "weather_list.html"
    context_object_name = "measurement_list"

class WeatherDetailView(DetailView):
    model = Measurement
    template_name = "measurement_detail.html"

class MeasurementCreateView(CreateView):
    model = Measurement
    template_name = "measurement_new.html"
    fields = "__all__"

class MeasurementUpdateView(UpdateView):
    model = Measurement
    template_name = "measurement_edit.html"
    fields = "__all__"

class MeasurementDeleteView(DeleteView):
    model = Measurement
    template_name = "measurement_delete.html"
    success_url = reverse_lazy("weather_list")

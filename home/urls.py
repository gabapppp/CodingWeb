from django.urls import path
from .views import SourceCreateView

urlpatterns = [
    path('execute/', SourceCreateView.as_view(), name="create-source")
]

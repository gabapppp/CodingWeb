from django.urls import path
from .views import SourceCreateView, ExecuteView

urlpatterns = [
    path('source/', SourceCreateView.as_view()),
    path('execute/', ExecuteView.as_view())
]

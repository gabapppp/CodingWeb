from django.urls import path
from .views import CompileCodeView

urlpatterns = [
    path('code', CompileCodeView.as_view()),
]

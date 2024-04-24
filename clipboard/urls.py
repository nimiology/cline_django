from django.urls import path

from clipboard.views import CreateClipboardAPIView, GetClipboardAPIView

urlpatterns = [
    path('', CreateClipboardAPIView.as_view()),
    path('<slug>/', GetClipboardAPIView.as_view()),
]
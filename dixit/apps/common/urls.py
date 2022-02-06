from django.urls import path

from common.views import HomeTemplateView


urlpatterns = [
    path('', HomeTemplateView.as_view())
]

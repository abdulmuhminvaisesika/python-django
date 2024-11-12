from django.urls import path
from .views import PreferenceListCreateView

urlpatterns = [
    path('preference/', PreferenceListCreateView.as_view(), name='preference-list-create'),
]

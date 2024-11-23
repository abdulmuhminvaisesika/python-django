from django.urls import path
from .views import PreferenceListCreateView, PreferenceDetailView

urlpatterns = [
    path('preference/', PreferenceListCreateView.as_view(), name='preference-list-create'),
    path('preference/<str:user_id>/', PreferenceDetailView.as_view(), name='preference-detail'),

]

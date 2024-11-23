from django.urls import path
from .views import UserProfileListCreateView,UserProfileDetailView


urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<str:user_id>/', UserProfileDetailView.as_view(), name='profile-detail'),
]

from django.urls import path
from .views import UserProfileListCreateView,UserProfileDetailView, ProfileCreateView


urlpatterns = [
    path('profiles/', UserProfileListCreateView.as_view(), name='profile-list-create'),
    path('profile_update/', UserProfileDetailView.as_view(), name='profile-detail'),
    path('profile_create/', ProfileCreateView.as_view(), name='profile-create')
]

from django.urls import path
from .views import MatchingScoreView, UserMatchingRecomentaion, UpdateMachingStatus

urlpatterns = [
    path('calculate_matching_score/', MatchingScoreView.as_view(), name='calculate_matching_score'),
    path('recomended_users_for/<str:user_id>/', UserMatchingRecomentaion.as_view(), name='matching_scores'),
    path('update_matching_status/<str:user1>/<str:user2>/', UpdateMachingStatus.as_view(), name='update_matching_status'),

]
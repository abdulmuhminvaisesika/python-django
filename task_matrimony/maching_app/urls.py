from django.urls import path
from .views import MatchingScoreView, UserMatchingRecomentaion, UpdateMachingStatus

urlpatterns = [
    path('calculate_matching_score/', MatchingScoreView.as_view(), name='calculate_matching_score'),
    path('recomended_users_for/', UserMatchingRecomentaion.as_view(), name='matching_scores'),
    path('update_matching_status/<str:user_id>/', UpdateMachingStatus.as_view(), name='update_matching_status'),

]
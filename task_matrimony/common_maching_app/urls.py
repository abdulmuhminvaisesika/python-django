# common_maching_app/urls.py
from django.urls import path
from .views import CommonMatchingListCreateView, CommonMatchingDetailView, CommonMatchingOptionsView

urlpatterns = [
    path('common-matching/', CommonMatchingListCreateView.as_view(), name='common-matching-list-create'),
    path('common-matching/<int:pk>/', CommonMatchingDetailView.as_view(), name='common-matching-detail'),
    path('options/<str:field_type>/', CommonMatchingOptionsView.as_view(), name='common-matching-options'),

]

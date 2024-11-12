from django.urls import path
from .views import *

urlpatterns = [
    path('matches/', MatchingView.as_view(), name='matches'),

]
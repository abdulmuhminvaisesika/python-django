from django.urls import path
from .views import UserView, LoginView, LogoutView, UserOperationByID

urlpatterns = [
    path('users/', UserView.as_view(), name='user-list-create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/<int:employee_id>/', UserOperationByID.as_view(), name='user-retrieve-update-delete')
]

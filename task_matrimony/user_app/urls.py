from django.urls import path
from .views import UserCrudOperation, LoginView, LogoutView, UserCrudOperationByID




urlpatterns = [
    path('user/', UserCrudOperation.as_view(), name='user_crud'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user/<str:user_id>/', UserCrudOperationByID.as_view(), name='user_crud_pk')

]


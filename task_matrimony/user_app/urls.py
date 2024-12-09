from django.urls import path
from .views import UserCrudOperation, LoginView, LogoutView, UserCrudOperationByID, GetAllUserByAdmin




urlpatterns = [
    path('user/', UserCrudOperation.as_view(), name='user_crud'),
    path('get_all/', GetAllUserByAdmin.as_view(), name='user_crud_all'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_token/', UserCrudOperationByID.as_view(), name='user_crud_pk')

]

